from app.models import User, Project, Role, UserProject

def test_create_user(db, projects, roles):
    # Simple create object
    user = User(name="User test", email="test@test.cl", hashed_password="hasdhhhshhh")
    db.add(user)
    db.commit()
    assert db.query(User).count() == 1
    #relations
    user_project = UserProject(role=roles[1])
    user_project.project = projects[0]
    user.projects.append(user_project)
    assert user.projects[0].project == projects[0]

def test_create_projects(db, users, roles):
    #simple create object
    project = Project(title="Los miseros", description="Proyecto que comprende...")
    db.add(project)
    db.commit()
    assert db.query(Project).count() == 1
    #relations
    user_project = UserProject(role=roles[1])
    user_project.user = users[0]
    project.users.append(user_project)
    assert project.users[0].user == users[0]

def test_create_user_projects(db, users, roles, projects):
    # Create an object
    user_project = UserProject(user=users[0], project=projects[0], role=roles[1])
    db.add(user_project)
    db.commit()
    db.refresh(user_project)
    # test the relations
    assert db.query(UserProject).count() == 1
    assert user_project.user == users[0]
    assert user_project.project == projects[0]
    assert user_project.role.role == roles[1].role
