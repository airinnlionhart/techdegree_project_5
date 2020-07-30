import datetime
from peewee import IntegerField, TextField, DateTimeField, SqliteDatabase, Model

#  peewee-3.13.3

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_id = IntegerField(primary_key=True)
    title = TextField()
    timespent = IntegerField()
    whatilearn = TextField()
    resourcestoremember = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

    @classmethod
    def add(cls, title, timespent, whatilearn, resourcestoremember, date):
        with DATABASE.transaction():
            cls.create(title=title, timespent=timespent,
                       whatilearn=whatilearn, resourcestoremember=resourcestoremember, date=date)


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
    # Entry.add(title="Entered", timespent=1, whatilearn="things", resourcestoremember="more things",
    #                  date="2020-07-30")
