from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import UserProgress

from pydantic import BaseModel




router = APIRouter()



class UserProgressRequest(BaseModel):

    user_id:str

    skill_id:int

    status:str


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get("/user_progress")

def get_user_progress(

    db: Session = Depends(get_db)

):

    data = db.query(
        UserProgress
    ).all()

    return data


@router.post("/user_progress")

def add_user_progress(

    request: UserProgressRequest,

    db: Session = Depends(get_db)

):

    progress = UserProgress(

        user_id=request.user_id,

        skill_id=request.skill_id,

        status=request.status

    )

    db.add(progress)

    db.commit()

    db.refresh(progress)

    return {

        "message":"Progress Saved"

    }

