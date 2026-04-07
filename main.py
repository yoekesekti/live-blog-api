from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
import jwt

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

security = HTTPBearer()

SECRET_KEY = "kunci-rahasia-kampus"
ALGORITHM = "HS256"

users_db = []
message_database = []

class User(BaseModel):
    username: str
    password: str

class Message(BaseModel):
    content: str
    author: str = "Anonim"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.post("/api/register")
def register(user: User):
    for u in users_db:
        if u.username == user.username:
            raise HTTPException(status_code=400, detail="Username sudah ada")
    users_db.append(user)
    return {"message": "Register berhasil"}

@app.post("/api/login")
def login(user: User):
    for u in users_db:
        if u.username == user.username and u.password == user.password:
            token = create_access_token({"sub": user.username})
            return {"access_token": token}
    raise HTTPException(status_code=401, detail="Login gagal")

@app.post("/api/blogs")
def add_message(msg: Message, auth: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(auth.credentials, SECRET_KEY, algorithms=[ALGORITHM])

        new_msg = {
            "content": msg.content,
            "author": msg.author if msg.author.strip() != "" else "Anonim",

            "real_user": payload.get("sub"),

            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        message_database.append(new_msg)

        return {
            "message": "Posting berhasil",
            "data": new_msg
        }

    except:
        raise HTTPException(status_code=403, detail="Token tidak valid atau kadaluwarsa!")

@app.get("/api/blogs")
def get_messages():
    return message_database
