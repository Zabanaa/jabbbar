<img src="https://github.com/Zabanaa/jabbbar/blob/develop/Jabbbar.png"
style="display: block; margin: 0 auto;">

# Jabbbar

Jabbbar is a wrapper for the Dribbble API. It is written in Python 3 and it's designed to
help you interface with the resources and content served by Dribbble. It will allow you to
effortlessly make calls.

_Please note that you are limited to 60 requests per minute and 1440 requests per day (for
calls using OAuth)_

# Requirements

Before you start using Jabbbar, please ensure you have registered an application with
Dribbble on their [developers site][1].
Give your application a name, a description, a url and a callback url (which will be used to
redirect your users after they agree to give you access to their information)
You will then get two keys: a **client id** and a **client secret**. Make note of
those as you will need both to request an access token.

_Be careful not to share your client secret publicly_

[1]: http://developer.dribbble.com/
