# Bottle SSLify

This is a simple Bottle extension that configures your Bottle application to redirect all incoming HTTP requests to HTTPS.

## Usage

Hello World:

    import bottle
    from bottle_sslify import SSLify

    app = bottle.Bottle()
    SSLify(app)


HTTP requests are redirected to HTTPS:

    $ curl -I http://localhost:7777
    HTTP/1.1 302 Found
    Content-Length: 0
    Content-Type: text/html; charset=UTF-8
    Location: https://localhost:7777/
    Date: Wed, 23 Jan 2013 09:34:50 GMT

## Installation

    $ pip install Bottle-SSLify
