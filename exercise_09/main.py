from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Filters(BaseModel):
    type: str
    published_after: str

@app.post("/filters/")
def apply_filters(filters: Filters):
    return {"filters": filters}

# Chạy server
if __name__ == "__main__":
    import uvicorn  
    uvicorn.run(app, host="127.0.0.1", port=8003)