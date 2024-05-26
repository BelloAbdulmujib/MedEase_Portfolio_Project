import pytest
from app import create_app, db
from app.models import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('config.TestConfig')

    # Create a test client using the Flask application configured for testing
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests
    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table(s)
    db.create_all()

    # Insert user data
    user1 = User(username='testuser1', email='test1@example.com')
    user1.set_password('Password1')
    user2 = User(username='testuser2', email='test2@example.com')
    user2.set_password('Password2')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
