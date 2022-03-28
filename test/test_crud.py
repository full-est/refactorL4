from app import crud, schemas, models


def test_get_user_by_email(db, users):
    assert users[0] == crud.get_user_by_email(db, users[0].email)


def test_create_user(db):
    assert 0 == db.query(models.User).count()
    crud.create_user(db, schemas.UserCreate(
        email="test@test.cl", name="names", password="test12333"))
    assert 1 == db.query(models.User).count()


def test_authenticate_user(db, users):
    assert users[0] == crud.authenticate_user(
        db, email=users[0].email, password="Test12345")


def test_update_user(db, users):
    crud.update_user(db, users[0], schemas.UserUpdate(name="Testa"))
    assert "Testa" == users[0].name


def test_create_project(db, users, roles):
    assert 0 == db.query(models.Project).count()
    crud.create_project(db, users[1], schemas.ProjectBase(
        title="Titulo", description="Descripcion asdasd"))
    assert 1 == db.query(models.Project).count()


def test_show_project(db, projects, users):
    assert projects[0] == crud.show_project(db, users[0], 1)


def test_show_projects(db, projects, users):
    assert projects == crud.show_projects(db, users[0])
    # test pagination
    assert [projects[1]] == crud.show_projects(db, users[0], 1, 2)
    # test filter query param
    assert [projects[1]] == crud.show_projects(
        db=db, current_user=users[0], q="segundo")
