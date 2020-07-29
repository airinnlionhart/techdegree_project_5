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
    return render_template('index.html')

@app.route('/entries')
def entries():
    return render_template('index.html')

@app.route('/entries/new', methods=('GET','POST'))
def new_entries():
    form = forms.CreateEntryForm()
    if form.validate_on_submit():
        models.Entry.add(journal_title=form.journal_title.data,time_spent=form.time_spent.data,learned=form.learned.data,
                         remember=form.remember.data, date_time=form.date_time.data)
        flash("validated")
        return render_template('new.html', form=form)
    else:
        print(str(form.journal_title.data) + str(form.learned.data) + str(form.remember.data))
        print(form.date_time.data)

    return render_template('new.html', form=form)


@app.route('/entries/<id>')
def get_entries():
    return render_template('detail.html')

@app.route('/entries/<id>/edit')
def edit_entries():
    return render_template('edit.html')

@app.route('/entries/<id>/delete')
def delete_entries():
    return render_template('edit.html')

if __name__ == '__main__':
    models.initialize()
    try:
        models.Entry.add(journal_title="Entered", time_spent=1, learned="things", remember="more things", date_time=datetime.datetime.now())

    except:
        print("failed to create")


