from fastapi import FastAPI
from app.routers import users, auth, projects


app = FastAPI(title="ExampleOfFastAPI")

# ROUTERS
app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
app.include_router(projects.router, prefix="/projects")


@app.get("/", tags=["HealthCheck"])
def root():
    return { "status": "Running." }
