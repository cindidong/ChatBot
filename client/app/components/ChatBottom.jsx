"use client";

import React, { useState } from "react";

const ChatBottom = ({ sendRequest, getLastBotMessage }) => {
  const [value, setValue] = useState("");

  const handleSendMessage = async (e) => {
    e.preventDefault();

    if (value.trim() === "") {
      alert("Enter valid message!");
      return;
    }

    let lastBotMessage = await getLastBotMessage();
    console.log(lastBotMessage);

    // after interaction with customer service agent, need server response
    // if server needs a response, clients needs one
    // if server doesn't need a response, client doesn't need one
    if (value.toLowerCase() == "cars") {
      await sendRequest(value, true, "car");
    } else if (value.toLowerCase().includes("thank")) {
      await sendRequest(value, true, "service");
    } else if (lastBotMessage && lastBotMessage.needResponse) {
      await sendRequest(value, true, lastBotMessage.surveyType);
    } else {
      await sendRequest(value, false, "");
    }
    setValue("");
  };

  return (
    <form
      onSubmit={handleSendMessage}
      className="container mx-auto max-w-4xl flex"
    >
      <input
        value={value}
        onChange={(e) => setValue(e.target.value)}
        className="input w-full focus:outline-none rounded-r-none"
        type="text"
      />
      <button
        type="submit"
        className="w-auto bg-gray-500 text-white rounded-r-lg px-5 text-sm"
      >
        Send
      </button>
    </form>
  );
};

export default ChatBottom;
