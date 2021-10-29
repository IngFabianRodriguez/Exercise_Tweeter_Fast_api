# Python
# Pydantic
# FastAPI
from fastapi import FastAPI
from fastapi import status


# Models
from models import User, UserIn, UserOut
from models import Tweet

app = FastAPI()


@app.get(path="/", tags=["Home"], status_code=status.HTTP_200_OK)
def home():
    """Base home, Comprobacion API funcionando"""
    return {"message": "Welcome"}
