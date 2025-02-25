from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
def check_item_availability(item_id: int, store_id: Optional[int] = None):
    # Giả sử kiểm tra tính khả dụng
    if store_id:
        return {"item_id": item_id, "store_id": store_id, "available": True}
    return {"item_id": item_id, "available": True}

# Chạy server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8005)