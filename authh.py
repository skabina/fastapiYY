from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from authx import AuthXConfig, AuthX

app = FastAPI()

config = AuthXConfig()
config.JWT_SECRET_KEY = "SECRET_KEY"
config.JWT_ACCESS_COOKIE_NAME = "access_token"
config.JWT_TOKEN_LOCATION = ["cookies"]

security = AuthX(config=config)


class UserLoginSchema(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(creds: UserLoginSchema):
    if creds.username == "test" and  creds.password == "test":
        token = security.create_access_token(uid="11111")
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

@app.get("/protected")
def protected():
    ...     


if __name__ == '__main__':
    uvicorn.run('authh:app', port=8000, reload=True)