from fastapi import FastAPI, HTTPException

app = FastAPI()

valid_statuses = ["pending", "completed", "canceled"]

@app.get("/status/")
def get_status(status: str):
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
    return {"message": f"Your request status is: {status}"}

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)