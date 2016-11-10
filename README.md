# Zabbbana

Simple to use python wrapper for the Dribbble API.

## Class Zabbbana

### Params

- client id
- client secret
- redirect_uri
- scope (list)
- state (randomly generated token)

### methods
- generate_auth_url
- get_access_token

======================

## Class Bucket

### Params

- bucket_id

### methods

- Bucket.get_details() // DONE
- Bucket.getShots() // DONE
- Bucket.addShot(id)
- Bucket.deleteShot(id)

======================

## Class Project

### Params

- project_id

### methods

- Project.get_details()
- Project.get_shots()

======================

## Class Shots

### Params

- No Params

### methods

- Shots.list_all()
- Shots.get_one(id)
- Shots.create(id)
- Shots.update(id)
- Shots.delete(id)

======================

## Class Shot

### Params

- shot_id

### methods

- Shot.get_attachements()
- Shot.create_attachement()
- Shot.get_single_attachement()
- Shot.delete_attachement()
- Shot.get_bucket_list()
- Shot.get_comments()
- Shot.get_comment_likes()
- Shot.get_single_comment()
- Shot.update_comment()
- Shot.delete_comment()
- Shot.do_I_like_a_comment()
- Shot.like_comment()
- Shot.unlike_comment()
- Shot.get_likes()
- Shot.do_I_like_a_shot()
- Shot.like()
- Shot.unlike()
- Shot.list_all_projects()
- Shot.get_rebounds()


======================

## Class Teams

### Params

- team_id

### methods

- Team.get_players()
- Team.get_shots()

======================

## Class User

### Params

- user_id or authenticated user

### methods

- User.get_details()
- User.get_user_details()
- User.get_buckets()
- User.list_followers()
- User.list_followed_users()
- User.list_shots_by_followed_users()
- User.do_i_follow_them()
- User.are_they_following_that_user()
- User.follow_player()
- User.unfollow_player()
- User.get_my_likes()
- User.get_likes()

- User.list_my_projects()
- User.list_projects()
- User.list_my_shots()
- User.list_shots()
- User.list_my_teams()
- User.list_shots()
- User.list_my_teams()
- User.list_teams()
- User.create_bucket()
- User.delete_bucket()
- User.update_bucket()




