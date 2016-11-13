# Zabbbana

Simple to use python wrapper for the Dribbble API.

## Class Zabbbana (DONE)

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

## Class Bucket (DONE)

### Params

- bucket_id

### methods

- Bucket.get_details() // DONE
- Bucket.create()   // DONE
- Bucket.update()   // DONE
- Bucket.delete()   // DONE
- Bucket.list-shots() // DONE
- Bucket.add_shot(id) // DONE
- Bucket.delete_shot(id) // DONE

======================

## Class Project (DONE)

### Params

- project_id

### methods

- Project.get_details() // DONE
- Project.get_shots()   // DONE

======================

## Class Shots (DONE)

### Params

- No Params

### methods

- Shots.list_all()  // DONE
- Shots.get_one(id) // DONE
- Shots.create(id)  // NEED A PLAYER ACCOUNT
- Shots.update(id)  // NEED A PLAYER ACCOUNT
- Shots.delete(id)  // NEED A PLAYER ACCOUNT

======================

## Class Shot (DONE)

### Params

- shot_id

### methods

- Shot.get_attachements()           // DONE
- Shot.get_single_attachement()     // DONE
- Shot.get_bucket_list()            // DONE
- Shot.get_comments()               // DONE
- Shot.get_comment_likes()          // DONE
- Shot.get_single_comment()         // DONE
- Shot.do_I_like_a_comment()        // DONE
- Shot.like_comment()               // DONE
- Shot.unlike_comment()             // DONE
- Shot.get_likes()                  // DONE
- Shot.do_I_like_a_shot()           // DONE
- Shot.like()                       // DONE
- Shot.unlike()                     // DONE
- Shot.list_all_projects()          // DONE
- Shot.get_rebounds()               //DONE


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

// Possibly not
- User.create_bucket()
- User.delete_bucket()
- User.update_bucket()

=======================

## Todo

_Need a player account_
- [ ] Shots.upload
- [ ] Shots.update
- [ ] Shots.delete

- [ ] Shot.create_attachement
- [ ] Shot.delete_comment
- [ ] Shot.create_comment
- [ ] Shot.update_comment
- [ ] Shot.delete_comment
