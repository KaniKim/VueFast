import datetime
from typing import List
import uuid

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import security.security as security
from sqlalchemy.orm import Session

from models.database import SessionLocal
from domain.schemas import Token, Post, User, PostDetail
import models.models as models

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.router.redirect_slashes = False


@app.post("/token", response_model=Token)
async def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = security.authenticate_user(db, form_data.username, form_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = datetime.timedelta(minutes=security.settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.user_id}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(security.get_current_active_user)):
    return current_user


@app.get("/users/me/itmes/")
async def read_own_items(current_user: User = Depends(security.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.user_id}]


@app.get("/api/post/list/", response_model=List[Post])
async def get_post_list(db: Session = Depends(get_db)):
    post = db.query(models.Post).all()
    return post


@app.get("/api/post/detail/{pk}", response_model=PostDetail)
async def post_post(pk: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == pk).first()

    return post


@app.post("/api/post/detail", response_model=PostDetail)
async def post_post(post: Post, db: Session = Depends(get_db)):
    post = models.Post(
        title=post.title,
        description=post.description,
        content=post.content,
        created_at=datetime.datetime.now(),
        modified_at=datetime.datetime.now(),
        owner_id=str(uuid.uuid4()),
    )
    db.add(post)
    db.commit()

    return post
