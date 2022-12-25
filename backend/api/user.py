from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Query, Response

from api import SessionLocal, get_db
from dto.user import UserRequest, UserResponse
from services.user import UserService
from services.security import Password, Auth


router = APIRouter(prefix="/user", tags=["users"])
user_service = UserService()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
@router.get("/", status_code=status.HTTP_200_OK)
async def create_user(
    user_info: UserRequest | None = None,
    email: str | None = Query(default=None),
    db: Session = Depends(get_db),
):
    if not user_info and email:
        user_existed = await user_service.get_user_existed_or_not(email=email, db=db)

        if user_existed:
            return Response(status_code=status.HTTP_200_OK)
        elif not user_existed:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=False)

    if user_info and not email:
        result = await user_service.create_user(
            email=user_info.email,
            password=user_info.password,
            name=user_info.name,
            db=db,
        )

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Email is already existed"
            )
        return result

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
