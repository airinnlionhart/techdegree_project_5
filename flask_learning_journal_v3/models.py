import datetime
from peewee import IntegerField, TextField, DateField, SqliteDatabase, Model
#  peewee-3.13.3

DATABASE = SqliteDatabase('journal.db')


class Entry(Model):
    journal_id = IntegerField(primary_key=True)
    title = TextField(null=False)
    timespent = IntegerField(null=False)
    whatilearn = TextField(null=False)
    resourcestoremember = TextField(null=False)
    date = DateField(default=datetime.datetime.now().strftime("%B %d, %Y"))

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


if __name__ == '__main__':
    initialize()
    view_all()
    # Entry.add(title="What I Have Learned", timespent=100, whatilearn="This has been a journey I have learned so much from Team Treehouse. I have progessed not only in Python but as Developer all around",
    #           resourcestoremember="This list would be so long but I hope to remember everything",
    #                    date="2020-07-30")
