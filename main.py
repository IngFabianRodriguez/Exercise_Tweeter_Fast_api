# Python
from typing import List

# Pydantic
# FastAPI
from fastapi import FastAPI
from fastapi import status


# Models
from models import UserBase, UserLogin, User
from models import Tweet

app = FastAPI()

# * Path Operators
@app.get(path="/active", tags=["Home"], status_code=status.HTTP_200_OK, summary="Home")
def home():
    """Base home, Comprobacion API funcionando"""
    return {"message": "Welcome"}


## * Path Operators for User

### * Register a User
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register User",
    tags=["Users"],
)
def singup():
    """Register User"""
    pass


### * Login a User
@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login User",
    tags=["Users"],
)
def login():
    """Login User"""
    pass


### * Show all Users
@app.post(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Show all Users",
    tags=["Users"],
)
def show_all_users():
    """List users system"""
    pass


### * Show a User
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Show a User",
    tags=["Users"],
)
def show_a_user():
    """Show user in system"""
    pass


### * Delete a User
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a User",
    tags=["Users"],
)
def delete_a_user():
    """Delete user in system"""
    pass


### * Update a User
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"],
)
def update_a_user():
    """Update user in system"""
    pass


## * Path Operators for Tweets

### * Show all Tweets
@app.post(
    path="/",
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"],
)
def home():
    """Show all Tweets"""
    pass


### * Post all Tweets
@app.post(
    path="/post",
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"],
)
def post_tweet():
    """Post a Tweet"""
    pass


### * Post all Tweets
@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Show a Tweet",
    tags=["Tweets"],
)
def show_a_tweet():
    """Show a Tweet"""
    pass


### * Delete a Tweet
@app.delete(
    path="/tweets/{tweet_id}/delete",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"],
)
def delete_a_tweet():
    """Delete a Tweet"""
    pass


### * Update a Tweet
@app.put(
    path="/tweets/{tweet_id}/update",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="update a Tweet",
    tags=["Tweets"],
)
def update_a_tweet():
    """Update a Tweet"""
    pass
