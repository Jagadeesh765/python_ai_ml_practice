from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr,Field
app = FastAPI()
@app.get("/")
def home():
    return {"message":"API is running"}
class UserCreate(BaseModel):
    email:EmailStr
    password:str=Field(min_length=8, max_length=50)
class UserResponse(BaseModel):
    email:EmailStr
    message:str
@app.post("/register",response_model=UserResponse)
def register_user(user:UserCreate):
    if "password" in user.password.lower():
        raise HTTPException(status_code=400,detail="weak password")
    return {
        "email":user.email,
        "message":"registered sucessfully"
    }

