from fastapi import FastAPI,HTTPException
app = FastAPI()
@app.get("/")
def home():
    return {"message": "welcome!"}
students={
    1 : {"name":"jagadeesh", "age":23},
    2 : {"name":"sairam", "age":99}
}
@app.get("/student/{student_id}")
def student_details(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404,detail="student not found")
    return students[student_id]