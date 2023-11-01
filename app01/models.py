import datetime

from mongoengine import Document, EmbeddedDocument, StringField, BooleanField, DateTimeField, IntField, ListField, \
    EmbeddedDocumentField, SequenceField


class Choice(EmbeddedDocument):
    text = StringField(max_length=255, required=True)
    true = BooleanField(default=False, required=True)

    def __str__(self):
        return self.text

class Problem(Document):
    id = SequenceField(primary_key=True)
    text = StringField(max_length=255, required=True)
    time = DateTimeField(default=datetime.datetime.now, required=True)
    image = StringField(max_length=255, required=True)
    publisher = IntField(default=0, required=True)
    choice_ = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'collection': 'problem',
        'abstract': False,

    }
