from fastapi import FastAPI, HTTPException
from typing import List, Optional
import pandas as pd

app = FastAPI()

# Load the products from the CSV file
products_df = pd.read_csv("./exercise_12/products.csv")

@app.get("/products/{category_id}")
def get_products(category_id: int, sort_by: Optional[str] = "name", order: Optional[str] = "asc"):
    # Filter products by category_id
    filtered_products = products_df[products_df['category_id'] == category_id]

    if filtered_products.empty:
        raise HTTPException(status_code=404, detail="No products found for this category.")

    # Sort the products
    if sort_by in filtered_products.columns:
        filtered_products = filtered_products.sort_values(by=sort_by, ascending=(order == "asc"))

    # Convert the DataFrame to a list of dictionaries
    products_list = filtered_products.to_dict(orient="records")
    
    return {"category_id": category_id, "products": products_list}

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8006)