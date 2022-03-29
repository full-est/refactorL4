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
    q: Optional[str] = Query("%", description="Search", min_length=2, max_length=50, example=""),
    skip: int = Query(0, description="Skipt n records", ge=0),
    limit: int = Query(100, description="N records for page", ge=1, le=100),
    db:Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """
    ## Index projects.

    This function return a list of projects if the request user has the rigth access.

    """
    return crud.show_projects(db=db, current_user=current_user, skip=skip, limit=limit, q=q)

@router.get(
    summary="Show a project",
    path="/{project_id}",
    response_model=schemas.ProjectSchema,
    tags=["Project"])
def show(
    project_id: int = Path(...,description="Id of the project to get.", gt=0, example=1),
    db:Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """
    ## Show project.

    This function return a project if the request user has the rigth access.

    Parameters:
    - Path parameter:
        - **project_id: Int** -> Project id

    Return a project model.
    """
    project = crud.show_project(db, current_user, project_id)
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The project you are looking doesn't exists."
        )
    else:
        return project

@router.post(
    path="/",
    response_model=schemas.Project,
    tags=["Project"],
    status_code=status.HTTP_201_CREATED
)
def create(
    project: schemas.ProjectBase,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """
    ## Create a project.

    This function create a project based on the ProjectBase model.

    Parameters:
    - Body parameter:
        - **project: ProjectBase** -> Project body.

    Return the created project.
    """
    return crud.create_project(db=db, current_user=current_user, project=project)

# @router.put(
#     path="/{project_id}",
#     response_model=schemas.Project,
#     tags=["Project"]
# )
# def update(
#     project_id: int = Path(..., description="Id of project to update", gt=0, example=1),
#     db: Session = Depends(get_db),
#     current_user: schemas.User = Depends(get_current_active_user)
# ):
#     crud.show_project(db, current_user)
#     return {}
