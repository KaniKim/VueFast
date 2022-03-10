from sqlalchemy.orm import Session

from domain.schemas import User, Post
from models.models import User as ModelUser
from models.models import Post as ModelPost


def get_user(db: Session, user_id: int) -> User:
    return db.query(ModelUser).filter(ModelUser.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User:
    return db.query(ModelUser).filter(ModelUser.email == email).first()


def get_prev_post(db: Session, id: int) -> Post:

    if not id:
        return None

    prev_post = db.query(ModelPost).filter(ModelPost.id == (id - 1)).first()

    if prev_post is None:
        return None

    return prev_post


def get_next_post(db: Session, id: int) -> Post:
    next_post = db.query(ModelPost).filter(ModelPost.id == (id + 1)).filter()

    if next_post is None:
        return None

    return next_post
