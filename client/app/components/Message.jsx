import React from "react";


const Message = ({ message, sendRequest, getLastBotMessage }) => {
  const handleYes = async (e) => {
    e.preventDefault();
    let lastBotMessage = await getLastBotMessage();
    await sendRequest("yes", true, lastBotMessage.surveyType);
  };

  const handleNo = async (e) => {
    e.preventDefault();
    let lastBotMessage = await getLastBotMessage();
    await sendRequest("no", true, lastBotMessage.surveyType);
  };

  return (
    <div>
      <div className={`chat ${message.isBot ? "chat-start" : "chat-end"}`}>
        <div className="chat-image avatar">
          <div className="w-10 rounded-full">
            <img src={message.isBot ? "bot-avatar.png" : "user-avatar.png"} />
          </div>
        </div>
        <div className="chat-bubble">
          <div className="join join-vertical">
            {message.text}
            {message.needButton && (
              <button onClick={handleYes} className="btn btn-wide p5">
                Yes
              </button>
            )}
            {message.needButton && (
              <button onClick={handleNo} className="btn btn-wide p5">
                No
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Message;
