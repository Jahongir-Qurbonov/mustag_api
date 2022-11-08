import peewee as pw
from app.database import db
from datetime import datetime
from uuid import uuid4


class BaseModel(pw.Model):
    """Base model for all models"""
    class Meta:
        database = db


class FileDBModel(BaseModel):
    """Model for storing file metadata"""
    m_id = pw.CharField(unique=True, default=uuid4)
    filename = pw.CharField(unique=True)
    created = pw.DateTimeField()
    timestamp_sec = pw.IntegerField(default=300)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        return super(FileDBModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.filename)


db.create_tables([FileDBModel, ])
