from app import schemas

def test_role_schemas():
    role = schemas.Role(role="developer", id=1)
    assert role.role == "developer"
    assert role.id == 1

def test_user_project():
    role = schemas.Role(role="developer", id=1)
    user = schemas.User(id=1, name="andres", email="andres.ch@pm.me", is_active=True)
    project = schemas.Project(id=1, title="titul", description="description",private=True, active=True, starts=0 )
    user_project = schemas.UserProjectSchema(role_id=1, user_id=1, project_id=1, role=role, user=user,project=project )
    assert user_project.project.id == user_project.project_id
    assert user_project.user.id == user_project.user_id
    assert user_project.role.id == user_project.role_id

def test_user_schemas(db):
    user_create = schemas.UserCreate(name="andres", email="andres.ch@pm.me", password="Test12345")
    assert user_create.name == "andres"
    assert user_create.email == "andres.ch@pm.me"
    assert user_create.password == "Test12345"
