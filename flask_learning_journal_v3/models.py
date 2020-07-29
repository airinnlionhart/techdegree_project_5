import datetime
from peewee import IntegerField, TextField, DateTimeField, SqliteDatabase, Model

#  peewee-3.13.3

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_id = IntegerField(primary_key=True)
    journal_title = TextField()
    time_spent = IntegerField()
    learned = TextField()
    remember = TextField
    date_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, journal_title, time_spent, learned, remember, date_time):
        cls.create(journal_title=journal_title, time_spent=time_spent,
                   learned=learned, remember=remember, date_time=date_time)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry], safe=True)


def view_all():
    query = Entry.select().dicts()

    for stuff in query:
        print(stuff)


def edit():
    view_all()
    user_input = input("what journal entry would you like please select a number")

    for entries in Entry.select():
        if str(entries.journal_id) == user_input:
            user_text = input("Please enter your journal entry")
            try:
                Entry.update(journal_entry=user_text).where(Entry.journal_id == entries.journal_id).execute()
            except:
                print("something went wrong")
        else:
            pass


if __name__ == '__main__':
    initialize()
    view_all()
    # add({'journal_title': 'this is my first journal entry',
    #      'time_spent': 2,
    #      'learned': 'how to build apps with flask',
    #      'remember': 'a lot now that I think about it'
    #      })
