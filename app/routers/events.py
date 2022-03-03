from fastapi import APIRouter

router = APIRouter()

@router.get("/events/", tags=["events"])
async def read_events():
    return [{"name": "The electroritms"}, {"name": "My Birthday"}]
