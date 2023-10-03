export default class Message {
  id: number;
  text: string;
  isBot: boolean;
  needResponse: boolean;
  needButton: boolean;
  surveyType: string;

  constructor(id: number, message: string, isBot: boolean, needResponse: boolean, needButton: boolean, surveyType: string) {
    this.id = id;
    this.text = message;
    this.isBot = isBot;
    this.needResponse = needResponse;
    this.needButton = needButton;
    this.surveyType = surveyType;
  }

  getID() {
    return this.id;
  }

  setID(newID: number) {
    this.id = newID
    return this.id;
  }

  getText() {
    return this.text;
  }

  setText(newText: string) {
    this.text = newText
    return this.text;
  }

  getIsBot() {
    return this.isBot;
  }

  setIsBot(newIsBot: boolean) {
    this.isBot = newIsBot
    return this.isBot;
  }

  getNeedResponse() {
    return this.needResponse;
  }

  setNeedResponse(newNeedResponse: boolean) {
    this.needResponse = newNeedResponse
    return this.needResponse;
  }

  getNeedButton() {
    return this.needButton;
  }

  setNeedButton(newNeedButton: boolean) {
    this.needButton = newNeedButton
    return this.needButton;
  }

  getSurveyType() {
    return this.surveyType;
  }

  setSurveyType(newSurveyType: string) {
    this.surveyType = newSurveyType
    return this.surveyType;
  }
}
