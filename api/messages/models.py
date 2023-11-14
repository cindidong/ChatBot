from api.database import db
from sqlalchemy import inspect

class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    text = db.Column(db.String())
    isBot = db.Column(db.Boolean)
    needResponse = db.Column(db.Boolean)
    needButton = db.Column(db.Boolean)
    surveyType = db.Column(db.String())

    def __init__(self, text: str, isBot: bool, needResponse: bool, needButton: bool, surveyType: str):
        self.text = text
        self.isBot = isBot
        self.needResponse = needResponse
        self.needButton = needButton
        self.surveyType = surveyType
        
    def get_by_id(id):        
        db_user = Messages.query.filter(Messages.id == id).first()
        return db_user
    
    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return '<id {}>'.format(self.id)
