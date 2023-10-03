"use client";

import React, { useState, useEffect } from "react";
import ChatBox from "./components/ChatBox.jsx";
import NavBar from "./components/NavBar.jsx";
import ChatBottom from "./components/ChatBottom.jsx";

export default function Home() {
  const [messages, setMessages] = useState([]);

  async function handleState() {
    await fetch("/api/messages")
      .then((res) => res.json())
      .then((data) => {
        setMessages(data);
      });
  }

  async function getLastBotMessage() {
    // retrieving last bot message to see if client needs to respond
    let lastBotMessage = "";
    let messages = await fetch("/api/messages").then((res) => res.json());

    for (var i = messages.length - 1; i >= 0; i--) {
      if (messages[i].isBot) {
        lastBotMessage = messages[i];
        return lastBotMessage;
      }
    }
    return null;
  }

  function generatePayload(textValue: string, needResponseValue: boolean, surveyValue: string) {
    return {
      id: 1.0,
      text: textValue,
      isBot: false,
      needResponse: needResponseValue,
      needButton: false,
      surveyType: surveyValue,
    };
  }

  async function sendRequest(textValue: string, needResponseValue: boolean, surveyValue: string) {
    let data = generatePayload(textValue, needResponseValue, surveyValue);
    console.log(JSON.stringify(data));

    let result = await fetch("/api/messages", {
      method: "POST",
      mode: "cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.ok) {
          handleState()
        }
        else {
          throw new Error(response.statusText);
        }
      })
      .catch((error) => {
        console.log(error);
      });
    return result;
  }

  // User has switched away from the tab (AKA tab is hidden)
  async function onBlur() {
    console.log("Tab is blurred");
    await sendRequest("", true, "product");
  }

  useEffect(() => {
    window.addEventListener("blur", onBlur);
    // Specify how to clean up after this effect:
    return () => {
      onBlur();
      window.removeEventListener("blur", onBlur);
    };
  }, []);

  return (
    <div className="flex flex-col mx-auto h-screen max-w-full">
      <header className="text-white text-center">
        <NavBar></NavBar>
      </header>
      <main className="flex-1 overflow-y-auto p-5">
        <ChatBox
          messages={messages}
          sendRequest={sendRequest}
          getLastBotMessage={getLastBotMessage}
        ></ChatBox>
      </main>
      <footer className="py-5 bg-gray-700 text-center text-white">
        <ChatBottom
          sendRequest={sendRequest}
          getLastBotMessage={getLastBotMessage}
        ></ChatBottom>
      </footer>
    </div>
  );
}
