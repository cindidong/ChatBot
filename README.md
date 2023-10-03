## Introduction
Simple Chatbot to gather reviews from customers. Scans for "thank you" in the customer chat message (likely to be a response to a customer service interaction), then starts the service agent review process. Stores the chat messages in a JSON file on the local file system.

## How To Run Locally
```
cd client
```
```
npm install
```
```
npm run dev
```

Website is running on http://localhost:3000.
The Flask server is running on http://127.0.0.1:5328.

### Docker
```
docker build -t chatbot .
```
```
docker run -dp 127.0.0.1:3000:3000 chatbot
```

Website is running on http://localhost:3000.
