from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/products/{category_id}")
def get_products(category_id: int, sort_by: Optional[str] = "name", order: Optional[str] = "asc"):
    return {"category_id": category_id, "sort_by": sort_by, "order": order}

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8006)