from fastapi import FastAPI,Depends
from fastapi.security import APIKeyHeader

from middlewares.apikey_validation import validate_api_key

app = FastAPI(dependencies=[
    Depends(validate_api_key)
])

@app.get("/getItem",tags=["test"])
async def get_item():
    return {'key':''}