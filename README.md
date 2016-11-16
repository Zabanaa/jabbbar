<img src="https://github.com/Zabanaa/jabbbar/blob/develop/Jabbbar.png"
style="display: block; margin: 0 auto;">

# Jabbbar

Jabbbar is a wrapper for the Dribbble API. It is written in Python 3 and it's designed to
help you interface with the resources and content served by Dribbble. It will allow you to
effortlessly make calls.

_Please note that you are limited to 60 requests per minute and 1440 requests per day (for
calls using OAuth)_

## Requirements

Before you start using Jabbbar, please ensure you have registered an application with
Dribbble on their [developers site][1].

You will be asked to give your app a name, a description, a url and a callback url. (Which
will be used to redirect your users to your site after they agree to give you access to
their account information).

When your app is registered, You will be given two keys: a **client id** and a **client secret**. Make note of
those as you will need both to request an access token.

_Be careful NOT to share your client secret publicly_

[1]: http://developer.dribbble.com/

## Installation

You can easily install Jabbbar through pip by like so
```bash
pip install jabbbar
```

Depending on your setup and virtualenv settings you may need sudo privileges

## Usage

### Authentication

```python

import jabbbar

# Instantiate the client object
client  = jabbbar.Jabbbar(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET',
redirect_uri('https://yoursite.com/authorize')

# Generate an authorisation url for your application
auth_url = client.auth_url

```

Send your users to the `auth_url`. After they authorise your app, they will be redirected
to the `redirect_uri` you've set in the previous step. The url will contain a query
parameter of `code` that looks something like this:
`http://yoursite.com/your_redirect_url?code="CODE_RETURNED_IN_REDIRECT"`.

In your web application back-end, retrieve the code and use it to request an access_token.

```python
# Request an access token based on the code returned in the redirect
access_token = client.set_access_token("CODE_RETURNED_IN_REDIRECT")
```

You can also instantiate a client directly by passing it an access_token if you have one
```python
client = jabbbar.Jabbbar(access_token="YOUR_ACCESS_TOKEN")
```

With your access token set, you can start making calls to the API.

## Usage

Jabbbar exposes the following classes to help you create more readable code: `Bucket`,
`Project`, `Shot`, `Shots`, `Team`, `User`

Each of these classes represent a collection of resources accessible through the API


