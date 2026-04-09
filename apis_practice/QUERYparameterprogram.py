from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message":"calculator api is running"}
@app.get("/mathcalculations")
def calculator(a:int,b:int,op:str):
    if op=="add":
        res=a+b
    elif op=="sub":
        res=a-b
    elif op=="mul":
        res=a*b
    elif op=="power":
        res=a**b
    elif op=="div":
        res=a/b
    elif op=="remainder":
        res=a%b
    else:
        return {"error":"invalid!"}
    return {"result":res}

    