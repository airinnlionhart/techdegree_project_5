from flask import Flask, g, render_template, flash, redirect, url_for
#flask-1.1.2
import forms
import models
import datetime

Debug = True

app = Flask(__name__)
app.secret_key = "shrreasfass781!-adffa1"


@app.before_request
def befor_request():
    """Connect to the Database before each request"""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the Database after each request"""
    g.db.close()
    return response


@app.route('/')
def index():
    entry = models.Entry.select().order_by(models.Entry.date.desc())
    return render_template('index.html', entry=entry)


@app.route('/entries')
def entries():
    entry = models.Entry.select().order_by(models.Entry.date.desc())
    return render_template('index.html', entry=entry)


@app.route('/entries/new', methods=('GET','POST'))
def new_entries():
    try:
        form = forms.CreateEntryForm()
        print(str(form.validate_on_submit()))
        models.Entry.add(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                         resourcestoremember=form.ResourcesToRemember.data, date=form.date.data)
        print("after add" + str(form.validate_on_submit()))
        return redirect(url_for('index'))
    except:
        print("failed to validate form")
        print(str(form.validate_on_submit()))
    print(str(form.validate_on_submit()))
    return render_template('new.html')


@app.route('/entries/<id>')
def get_entries(id):
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<id>/edit', methods=('GET','POST'))
def edit_entries(id):

    form = forms.CreateEntryForm()
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    try:
        form.validate_on_submit()
        print("at here")
        models.Entry.update(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                     resourcestoremember=form.ResourcesToRemember.data, date=form.date.data).where(models.Entry.journal_id == id).execute()
        return redirect(url_for('index'))
    except:
        print(entry)
        print("failed to validate form")
        flash("something went wrong","error")
    return render_template('edit.html', entry=entry, form=form)

@app.route('/entries/<id>/delete')
def delete_entries(id):
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    try:
        models.Entry.delete().where(
            models.Entry.journal_id == id).execute()
        return redirect(url_for('index'))
    except:
        return redirect(url_for('index'), entry=entry)


if __name__ == '__main__':
    models.initialize()





