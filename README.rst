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

_Note: jabbbar is only compatible with python 3.3 and up_

You can easily install Jabbbar through pip by like so
```bash
pip install jabbbar
```

Depending on your setup and virtualenv settings you may need sudo privileges

## Usage

### Authentication

```python
from jabbbar import Jabbbar

# Instantiate the client object
client  = Jabbbar(client_id='CLIENT_ID', client_secret='CLIENT_SECRET', redirect_uri='https://yoursite.com/authorize')

# You can also pass optional scope and state params
client = Jabbbar(client_id='CLIENT_ID', client_secret='CLIENT_SECRET', scope=['write','upload'], state="somerandomsecretstring")

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
client = Jabbbar(access_token="YOUR_ACCESS_TOKEN")
```

With your access token set, you can start making calls to the API.

## Userless Access

Since version 0.2.0, you can make read-only requests against the API's public endpoints.

To do so, just copy your `client access token` (found in your application page on dribbble.com) and pass it to the client instance.

```python
client = Jabbbar(client_token="YOUR_CLIENT_TOKEN")
```
_Note that you will not be able to access protected resources with a userless client_

## Usage

Jabbbar exposes the following classes to help you create more readable code: `Bucket`,
`Project`, `Shot`, `Shots`, `Team`, `User`

Each of these classes represent a collection of resources accessible through the API

To use them, simply import them into your app like this

```python
from jabbar import Bucket, Project # etc ...
```

## Examples

### Users
Create a user object
```python
# ...
# Instantiate your client above
my_user = User(client)

```

```python
# Get your user's account details
my_user.get_details()

# Get another user's account details
my_user.get_details(username="therealmichaeljordan")
```

### Shots

```python
# Instantiate a Shots object
shots = Shots(client)

# List all shots
shots.list_all()

# Get a specific shot's details
shots.get_one(1234567890)
```

### Teams

```python
# Instantiate a Team object
my_team = Team(client, team_name="name_of_the_team")

# Get a list of all of the team players
my_team.list_players()

# You can also list the players for other teams
my_team.list_players(team_name="some_other_team")
```

### Projects

```python
# Instantiate a Project object
project = Project(client, project_id=1234567890)

# Get details for the instantiated project
project.get_details()

# You can also details for other projects
project.get_details(project_id=12345678980)
```

### Buckets

```python
# Instantiate a Bucket object
bucket = Bucket(client, bucket_id=1234567890)

# Get details for the instantiated bucket
bucket.get_details()

# Create a bucket
bucket.create(name="my_new_bucket", description="a cool bucket")
```

### Shots (individual shots)

```python
# Instantiate a Bucket object
shot = Shot(client, shot_id=1234567890)

# Get a list of all attachments for the instantiated shot
shot.list_attachments()

# Get a list of all attachments for another shot
shot.list_attachments(shot_id=9283328392)
```

## Full List Of Methods

```
User.get_details()
User.list_buckets()
User.list_shot_likes()
User.list_projects()
User.list_shots()
User.list_teams()
User.list_followers()
User.list_following()
User.list_shots_from_following()
User.check_following()
User.follow_user()
User.unfollow_user()

Team.list_players()
Team.list_shots()

Shots.list_all()
Shots.get_one()

Shot.list_attachments()
Shot.get_attachment()
Shot.list_buckets()
Shot.list_comments()
Shot.list_comment_likes()
Shot.get_comment()
Shot.check_user_likes_comment()
Shot.like_comment()
Shot.unlike_comment()
Shot.list_likes()
Shot.like()
Shot.unlike()
Shot.list_projects()
Shot.list_rebounds()
Shot.check_user_likes_shots()

Project.get_details()
Project.get_shots()

Bucket.get_details()
Bucket.create()
Bucket.update()
Bucket.delete()
Bucket.list_shots()
Bucket.add_shot()
Bucket.remove_shot()
```

## Testing

In order to run the tests, follow these 3 steps:

- Rename `jabbbar/tests/credentials.example.py` to `credentials.py`
- Fill in your credentials
- run `nosetests`


## Contribution and Improvements

If you spot code smells and wish to make improvements, please feel free to do so by way of
pull requests, explaining how the solution you're proposing is better (purely for learning
purposes)

## License

Jabbbar is licensed under the Do What The Fuck You Want license.

## Todo

- [ ] Create a `Jabbar.rate_limit()` method
- [ ] Create a `Jabbar.remaining_requests()` method

_Need a player account_
- [ ] `Shots.upload`
- [ ] `Shots.update`
- [ ] `Shots.delete`
- [ ] `Shot.create_attachement`
- [ ] `Shot.delete_comment`
- [ ] `Shot.create_comment`
- [ ] `Shot.update_comment`
- [ ] `Shot.delete_comment`

## Build Status
[![Build Status](https://travis-ci.org/Zabanaa/jabbbar.svg?branch=master)](https://travis-ci.org/Zabanaa/jabbbar)
