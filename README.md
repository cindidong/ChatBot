# Review Chat Bot
## Introduction
Interactive chat bot to gather reviews from customers. Scans for "thank you" in the customer chat message (simulates the end of a customer service interaction), then starts the service agent review process. If the user switches to another tab (simulates the process of a purchase/a cart check out), then the chat bot starts the product review process. Stores the chat messages in a JSON file on the local file system.

## How To Run Locally
### Postgres
#### Set Up Postgres
```
brew services start postgresql@14 (pgstart)
create database testdb;
create user testuser with encrypted password '1234';
grant all privileges on database testdb to testuser;
```

#### Migrate
```
cd api
flask --app index db init
flask --app index db migrate
flask --app index db upgrade
```

#### End
```
brew services stop postgresql@14 (pgend)
```

### Running Web Service
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
