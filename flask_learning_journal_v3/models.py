import datetime
from peewee import * 
#  peewee-3.13.3

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_id = IntegerField(primary_key=True)
    journal_entry = TextField()
    date_added = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)


def add(text):
    try:
        Entry.create(journal_entry=text)
    except:
        print("test")


def view_all():
    query = Entry.select()

    for stuff in query:
        print(stuff.journal_id, stuff.journal_entry, stuff.date_added)


def edit():

    view_all()
    user_input = input("what journal entry would you like please select a number")

    for entries in Entry.select():
        if str(entries.journal_id) == user_input:
            user_text = input("Please enter your journal entry")
            try:
                Entry.update(journal_entry = user_text).where(Entry.journal_id == entries.journal_id).execute()
            except:
                print("something went wrong")
        else:
            pass