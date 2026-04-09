from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "welcome to fastapi!"}
@app.get("/about")
def about_root():
    return {
        "name": "jagadeesh",
        "role": "AIML INTERN"
    }
