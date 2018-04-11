# RabbitMQ-Demo


## Intro

RabbitMQ is a message broker: it accepts and forwards messages. You can think about it as a post office: when you put the mail that you want posting in a post box, you can be sure that Mr. Postman will eventually deliver the mail to your recipient. In this analogy, RabbitMQ is a post box, a post office and a postman.

The major difference between RabbitMQ and the post office is that it doesn't deal with paper, instead it accepts, stores and forwards binary blobs of data ‒ messages.

## RabbitMQ Setup

### Ubuntu

For Ubuntu 16.04
Just update the repos and install using apt-get:

```
$ apt-get update
$ apt-get install rabbitmq-server
```
To start the server:

```
$ rabbitmq-server start
```

### Windows

For Windows, download the latest installer from: https://www.rabbitmq.com/download.html
and follow the usual steps to install it.

### Linux Container

This is best and portable option to setup Rabbitmq-server.
Just pull and run the container by running:

```
$ docker run -d --hostname my-rabbit --name some-rabbit rabbitmq:3
```

If you wish to change the default username and password of guest / guest, you can do so with the RABBITMQ_DEFAULT_USER and RABBITMQ_DEFAULT_PASS environmental variables:

```
$ docker run -d --hostname my-rabbit --name some-rabbit -e RABBITMQ_DEFAULT_USER=user -e RAB
```

Note: To install docker
    Just execute:

```
    $ sudo curl https://get.docker.com | sh
```

### Please browse to the sub-directories for example descriptions

## Authors

* **Prashant Piprotar** - - [Prash+](https://github.com/prashplus)

Visit my blog for more Tech Stuff
### http://www.prashplus.com
