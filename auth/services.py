from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from .models import Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_token(token: str = Depends(oauth2_scheme)):
    token_exists = await Token.filter(token=token).exists()
    if not token_exists:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )