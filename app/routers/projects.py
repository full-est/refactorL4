from fastapi import APIRouter, Depends, Request, HTTPException, status, Path, Query
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.dependencies import get_current_active_user, get_db
from typing import List, Optional

router = APIRouter()

@router.get(
    path="/",
    response_model=List[schemas.Project],
    tags=["Project"])
def index(
            q: Optional[str] = Query("%", description="Search", min_length=2, max_length=50),
            skip: int = Query(0, description="Skipt n records for pagination", ge=0),
            limit: int = Query(100, description="Records for page", ge=1, le=100),
            db:Session = Depends(get_db),
            current_user: schemas.User = Depends(get_current_active_user)
        ):
    return crud.show_projects(db=db, current_user=current_user, skip=skip, limit=limit, q=q)

@router.get(
    path="/{project_id}",
    response_model=schemas.ProjectSchema,
    tags=["Project"])
def show(
            project_id: int = Path(...,description="The iD of the project to get.", gt=0, example=1),
            db:Session = Depends(get_db),
            current_user: schemas.User = Depends(get_current_active_user)
        ):
    return crud.show_project(db, current_user, project_id)

@router.post("/", response_model=schemas.Project, tags=["Project"])
def create(
            project: schemas.ProjectBase,
            db: Session = Depends(get_db),
            current_user: schemas.User = Depends(get_current_active_user)
        ):
    return crud.create_project(db=db, current_user=current_user, project=project)
