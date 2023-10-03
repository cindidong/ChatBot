"use client";

import React, {useState, useEffect, useRef} from "react";
import Message from "./Message.jsx";

const ChatBox = ({ messages, sendRequest, getLastBotMessage }) => {
  /*
  const messagesEndRef = useRef();

  const scrollToBottom = () => {
    messagesEndRef.current.scrollIntoView({ behavior: "smooth"})
  };

  useEffect(scrollToBottom, [messages])
  */

  //       <div ref={messagesEndRef}></div>


  return (
    <div>
      {messages?.map((message) => (
        <Message key={message.id} message={message} sendRequest={sendRequest} getLastBotMessage={getLastBotMessage}/>
      ))}
    </div>
  );
};

export default ChatBox;
