# Python
from typing import Optional, List

# Pydantic
# FastAPI
from fastapi import FastAPI
from fastapi import status


# Models
from models import UserBase, UserLogin, User
from models import Tweet

app = FastAPI()

# * Path Operators
@app.get(path="/", tags=["Home"], status_code=status.HTTP_200_OK, summary="Home")
def home():
    """Base home, Comprobacion API funcionando"""
    return {"message": "Welcome"}


# * Path Operators for User
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
