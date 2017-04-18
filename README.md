# Ohsiha lunch
This is project work for course MAT-81000 (2017) of TUT.
 
## Lunch application


## Lunch API
### Topics list:
URL: https://ohsihalunch.herokuapp.com/lunch/api/topics/
* Methods: GET, POST
* Usage: List all available topics. Create new topic.
* Example (using httpie):
```shell
# GET
http https://ohsihalunch.herokuapp.com/lunch/topics/

# POST
http -a user:psw POST https://ohsihalunch.herokuapp.com/lunch/topics/ name="REST topic" text="This is some text."
```

### Topics details:
URL: https://ohsihalunch.herokuapp.com/lunch/api/topics/<topic_id>/
* Methods: GET, PUT, DELETE
* Usage: Show single topic. Update single topic. Delete single topic.
* Example (using httpie):
```shell
# GET
http https://ohsihalunch.herokuapp.com/lunch/topics/1/

# PUT
http -a user:psw PUT https://ohsihalunch.herokuapp.com/lunch/api/topics/1/ name="REST topic" text="This is some text. edited"

# DELETE
http -a user:psw DELETE https://ohsihalunch.herokuapp.com/lunch/api/topics/1/
```

### Comments list:
URL: https://ohsihalunch.herokuapp.com/lunch/api/topics/<topic_id>/comments/
* Methods: GET, POST
* Usage: List all available comments in single topic. Create new comment.
* Example (using httpie):
```shell
# GET
http https://ohsihalunch.herokuapp.com/lunch/topics/1/comments/

# POST
http -a user:psw POST https://ohsihalunch.herokuapp.com/lunch/topics/1/comments/1/ topic=1 text="comment text"
```

### Comments details:
URL: https://ohsihalunch.herokuapp.com/lunch/api/topics/<topic_id>/comments/<comment_id>/
* Methods: GET, PUT, DELETE
* Usage: Show single comment. Update single comment. Delete single comment.
* Example (using httpie):
```shell
# GET
http https://ohsihalunch.herokuapp.com/lunch/topics/1/comments/1/

# PUT
http -a user:psw POST https://ohsihalunch.herokuapp.com/lunch/topics/1/comments/1/ text="comment text" topic=1

# DELETE
http -a user:psw DELETE https://ohsihalunch.herokuapp.com/lunch/api/topics/1/comments/1
```
