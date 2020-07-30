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
    entry = models.Entry.select()
    return render_template('index.html', entry=entry)


@app.route('/entries')
def entries():
    entry = models.Entry.select()
    return render_template('index.html', entry=entry)


@app.route('/entries/new', methods=('GET','POST'))
def new_entries():
    form = forms.CreateEntryForm()
    try:
        form.validate_on_submit()
        models.Entry.add(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                         resourcestoremember=form.ResourcesToRemember.data, date=form.date.data)
        print("tried")
        return render_template('new.html', form=form)
    except:
        print("failed to validate form")
    return render_template('new.html', form=form)


@app.route('/entries/<id>')
def get_entries(id):
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<id>/edit')
def edit_entries(id):
    form = forms.CreateEntryForm()
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    try:
        form.validate_on_submit()
        entry.update(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                         resourcestoremember=form.ResourcesToRemember.data, date=form.date.data).where(models.Entry.journal_id == entry.journal_id).execute()
        return render_template('index.html', entry=entry, form=form)
    except:
        print("failed to validate form")
    return render_template('edit.html', form=form)

@app.route('/entries/<id>/delete')
def delete_entries():
    return render_template('edit.html')

if __name__ == '__main__':
    models.initialize()





