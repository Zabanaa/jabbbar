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

