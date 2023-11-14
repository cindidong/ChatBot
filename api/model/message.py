from marshmallow import Schema, fields, post_load


class Message(object):
    def __init__(self, id: int, text: str, isBot: bool, needResponse: bool, needButton: bool, surveyType: str):
        self.id = id
        self.text = text
        self.isBot = isBot
        self.needResponse = needResponse
        self.needButton = needButton
        self.surveyType = surveyType
    
    def getID(self):
        return self.id
    
    def setID(self, newID):
        self.id = newID
        
    def getText(self):
        return self.text
    
    def getIsBot(self):
        return self.isBot
    
    def setIsBot(self, newIsBot):
        self.isBot = newIsBot
    
    def getNeedResponse(self):
        return self.needResponse
    
    def setNeedResponse(self, newNeedResponse):
        self.needResponse = newNeedResponse
    
    def getNeedButton(self):
        return self.needButton
    
    def setNeedButton(self, newNeedButton):
        self.needButton = newNeedButton
    
    def getSurveyType(self):
        return self.surveyType
    
    def setSurveyType(self, newSurveyType):
        self.surveyType = newSurveyType



class MessageSchema(Schema):
    id = fields.Int()
    text = fields.Str()
    isBot = fields.Bool()
    needResponse = fields.Bool()
    needButton = fields.Bool()
    surveyType = fields.Str()
    
    @post_load
    def make_request(self, data, **kwargs)->Message:
        return Message(**data)
    