from flask import Flask, g, render_template, redirect, url_for
# flask-1.1.2
import forms
import models
from flask_wtf.csrf import CsrfProtect

csrf = CsrfProtect()

Debug = True

app = Flask(__name__)
csrf.init_app(app)
app.secret_key = "shrreasfass781!-adffa1"


@app.before_request
def before_request():
    """Connect to the Database before each request"""
    db = models.DATABASE
    db.connect()


@app.after_request
def after_request(response):
    """Close the Database after each request"""
    models.DATABASE.close()
    return response


@app.route('/')
def index():
    entry = models.Entry.select().order_by(models.Entry.date.desc())
    return render_template('index.html', entry=entry)


@app.route('/entries')
def entries():
    entry = models.Entry.select().order_by(models.Entry.date.desc())
    return render_template('index.html', entry=entry)


@app.route('/entries/new', methods=('GET', 'POST'))
def new_entries():
    form = forms.CreateEntryForm()
    if form.validate_on_submit():
        models.Entry.add(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                         resourcestoremember=form.ResourcesToRemember.data, date=form.date.data)
        return redirect(url_for('index'))
    else:
        return render_template('new.html', form=form)


@app.route('/entries/<id>')
def get_entries(id):
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<id>/edit', methods=('GET', 'POST'))
def edit_entries(id):
    form = forms.CreateEntryForm()
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    if form.validate_on_submit():
        models.Entry.update(title=form.title.data, timespent=form.timeSpent.data, whatilearn=form.whatILearned.data,
                            resourcestoremember=form.ResourcesToRemember.data, date=form.date.data).where(
            models.Entry.journal_id == id).execute()
        return redirect(url_for('index'))
    return render_template('edit.html', entry=entry, form=form)


@app.route('/entries/<id>/delete')
def delete_entries(id):
    entry = models.Entry.select().where(models.Entry.journal_id == id)
    try:
        models.Entry.delete().where(
            models.Entry.journal_id == id).execute()
        return redirect(url_for('index'))
    except:
        return redirect(url_for('index'))


if __name__ == '__main__':
    models.initialize()
