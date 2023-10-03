# set base image (host OS)
FROM python:3.9

# Install netcat
RUN apt-get update && \
    apt-get -y install netcat-traditional && \
    apt-get -y install nodejs && \
    apt-get -y install npm && \
    apt-get clean

# set the working directory in the container
WORKDIR /usr/src/app

# copy the content of the local directory to the working directory
COPY . /usr/src/app

ENV PATH /usr/src/app/client/node_modules/.bin:$PATH

# set the working directory to client in the container
WORKDIR /usr/src/app/client

RUN npm install

EXPOSE 3000
CMD ["npm", "run", "dev"]