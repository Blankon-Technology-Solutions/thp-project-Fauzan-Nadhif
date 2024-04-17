# TAKE HOME PROJECT BLANKON TECHNOLOGY SOLUTIONS

First of all, congratulations on reaching this step in the interview series. The take-home project is mainly designed to assess how well you structure your code and how efficiently you build a solution for the given task.

## Requirements for the take home project:
- 🫙 Please utilize Docker for easy setup and testing on our side 🫙 
- 🧪 minimum 80% test coverage 🧪 
- 🐍 The project must be written in Python and utilize Django REST framework🐍
- ❗️ You must use your own third-party credentials, such as a Google API Key or LinkedIn API Key, for your local testing. However, please do not share them in any of these files; we will use our own credentials to test it. ❗️ 

# Simple Backend Todo App
## Create a backend service for a Todo App with the following specifications:
- user can login/signup using Linkedin SSO and Google SSO
- user can login/signup using an email and password combination
- user can list,add,update and delete their todos
- If a user is logged in with the same credentials on two or more browsers, when they add, update, or delete a todo in one browser, it should sync to all browsers via socket (push mechanism
- Except for login/signup, other APIs and socket connections must be protected.



## When you are done
- 🫸 push your code to this repository, or if you put it in different branch please merge to main branch 🫸
- 🏷️ Go to issues tab, you will have 1 open issue please label that issue to Ready to Review 🏷️ 

## Setup
- copy and rename .env.sample into .env and fill out the missing credentials
- pip install -r requirements.txt
- create psql database
- python manage.py migrate
- python manage.py runserver

## Setup with docker
- copy and rename .env.sample into .env and fill out the missing credentials
- run docker-compose up

## Unit test
- run python manage.py test

## Testing API locally

- Register user
```
curl --location 'http://127.0.0.1:8000/authentication/register' \
--header 'Content-Type: application/json' \
--data '{
    "email": "test@gmail.com",
    "password": "test",
    "confirm_password": "test"
}'
```

- Login
```
curl --location 'http://127.0.0.1:8000/authentication/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test@gmail.com",
    "password": "test"
}'
```

- Login with Google
Get authorization code from https://developers.google.com/oauthplayground/ or from
```
https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=<CALLBACK_URL_YOU_SET_ON_GOOGLE>&prompt=consent&response_type=code&client_id=<YOUR CLIENT ID>&scope=openid%20email%20profile&access_type=offline
```
Then use that for:
```
curl --location 'http://127.0.0.1:8000/authentication/google/' \
--header 'Content-Type: application/json' \
--data '{
    "code": "<YOUR_AUTHORIZATION_CODE>"
}'
```

- List Todos
```
curl --location 'http://127.0.0.1:8000/todos' \
--header 'Authorization: Bearer <YOUR_TOKEN>'
```

- Create Todo
```
curl --location 'http://127.0.0.1:8000/todos/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_TOKEN>' \
--data '{
    "title": "Test Todo",
    "description": "test todo"
}'
```

- Get Todo
```
curl --location 'http://127.0.0.1:8000/todos/1' \
--header 'Authorization: Bearer <YOUR_TOKEN>'
```

- Update Todo
```
curl --location --request PUT 'http://127.0.0.1:8000/todos/1/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <YOUR_TOKEN>' \
--data '{
    "title": "Test Todo updated",
    "description": "Test Todo updated"
}'
```

- Delete Todo
```
curl --location --request DELETE 'http://127.0.0.1:8000/todos/1/' \
--header 'Authorization: Bearer <YOUR_TOKEN>'
```

## Testing WebSocket

You can test the websocket functionaliy by opening localhost:8000/todos/test-ws in your browser. But first, replace the token in templates/test-ws.html (Note that if you are using docker that means you have to change the file from inside the container). Click connect WebSocket and then try calling the todos API.
