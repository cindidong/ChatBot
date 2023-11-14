from api.database import db
from sqlalchemy.dialects.postgresql import JSON

class Messages(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Float, primary_key=True)
    text = db.Column(db.String())
    isBot = db.Column(db.Boolean)
    needResponse = db.Column(db.Boolean)
    needButton = db.Column(db.Boolean)
    surveyType = db.Column(db.String())

    def __init__(self, id: float, text: str, isBot: bool, needResponse: bool, needButton: bool, surveyType: str):
        self.id = id
        self.text = text
        self.isBot = isBot
        self.needResponse = needResponse
        self.needButton = needButton
        self.surveyType = surveyType
        
    def get_by_id(id):        
        db_user = Messages.query.filter(Messages.id == id).first()
        return db_user

    def __repr__(self):
        return '<id {}>'.format(self.id)
