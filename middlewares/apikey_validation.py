from fastapi import security ,HTTPException, status,Request
from fastapi.security import api_key

apikey = "ylerWWelse[Xpze]t3rws"
api_key_header = api_key.APIKeyHeader(name="X-API-KEY",description="API Key value")

async def validate_api_key(req: Request,key:str = security(api_key_header)):
    print(req , key)
    if not(apikey == key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="missing or invalid API key"
        )
    return None
