from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int, details: Optional[str] = "basic"):
    if details == "full":
        return {"user_id": user_id, "details": "Full profile information"}
    return {"user_id": user_id, "details": "Basic information"}

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)