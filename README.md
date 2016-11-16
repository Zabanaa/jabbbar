<img src="https://github.com/Zabanaa/jabbbar/blob/develop/Jabbbar.png"
style="text-align:center">

## Usage

1. Register an app on Dribbble.com (choose a name, add a description, a website url and
  a callback url)
2. You'll get a client_id and client_secret (store them somewhere)
3. Download and import jabbbar
4. Instantiate a jabbbar object and pass it your client_id, client_secret and redirect_uri
5. Generate an autorisation link
6. Send the user to dribbble to access their account and agree to let the app use their
   information. If they accept, they will be redirected to your callback url with a code
   as a query param. Retrieve that code and store it in a variable for later use.
7. With the code retrieved, you can now get an access token to make requests on behalf of
   that user, by using jabbbar.get_access_token(code="GENERATED_CODE")
8. The access token is now set, you can start using the package to make requests

Things I learned

- The OAuth authentication flow
- Nosetests and how to use the framework
- How to correctly document code
- Composition vs Inheritance ("has a/uses a" vs "is a")

Simple to use python wrapper for the Dribbble API.

## Class Jabbbar (DONE)

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

## Class Teams (DONE)

### Params

- team_id

### methods

- Team.get_players()            // DONE
- Team.get_shots()              // DONE

======================

## Class User (DONE)

### Params

- user_id or authenticated user

### methods

- User.get_details()                    // DONE
- User.get_user_details()               // DONE
- User.get_buckets()                    // DONE
- User.list_followers()                 // DONE
- User.list_followed_users()            // DONE
- User.list_shots_by_followed_users()   // DONE
- User.do_i_follow_them()               // DONE
- User.are_they_following_that_user()   // DONE
- User.follow_player()                  // DONE
- User.unfollow_player()                // DONE
- User.get_my_likes()                   // DONE
- User.get_likes()                      // DONE
- User.list_my_projects()               // DONE
- User.list_projects()                  // DONE
- User.list_my_shots()                  // DONE
- User.list_shots()                     // DONE
- User.list_my_teams()                  // DONE
- User.list_shots()                     // DONE
- User.list_my_teams()                  // DONE
- User.list_teams()                     // DONE

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

- [ ] Request Exceptions
- [ ] Jabbbar.remaining_requests @property
- [ ] Jabbbar.rate_limit @property

