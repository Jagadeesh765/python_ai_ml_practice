###VALIDATES FOR EMAIL AND PASSWORD FORMAT
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field,field_validator
app = FastAPI()
class User(BaseModel):
    name:str=Field(min_length=5)
    email:EmailStr
    password:str=Field(min_length=9)
    age:int=Field(ge=15,le=21)
    @field_validator('password')
    def check_password(cls,value):
        if "@" not in value:
            raise ValueError("password must cantain @")
        return value
@app.post("/register/")
def register(user:User):
    return { "message": "user registred sucessfully",
            "data": user
    }
#########ADD VALIDATION RULES TO NOTES AND USER MODELS
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr,Field,field_validator
app = FastAPI()
class User(BaseModel):
    name:str=Field(min_length=5)
    email:EmailStr
    password:str=Field(min_length=9)
    age:int=Field(ge=15,le=21)
class Note(BaseModel):
    title:str=Field(min_length=5,max_length=10)
    password:str=Field(min_length=9,max_length=100)
@app.post("/user")
def create_user(user:User):
    return { "message": "user created sucessfully",
            "data": user
    }
@app.post("/note")
def create_note(note:Note):
    return { "message": "note create sucessfully",
            "data": note
    }
