from fastapi import FastAPI, HTTPException
from datetime import date

app = FastAPI()

@app.get("/validate_date/")
def validate_date(date_str: str):
    try:
        valid_date = date.fromisoformat(date_str)
        return {"message": f"The date is valid: {valid_date}"}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)