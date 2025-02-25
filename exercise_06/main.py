from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    birth_year: int

@app.post("/user/")
def create_user(user: User):
    age = 2025 - user.birth_year  # Giả sử năm hiện tại là 2025
    return {"message": f"Hello, {user.name}, you are {age} years old."}

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)