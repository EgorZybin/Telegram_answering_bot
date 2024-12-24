from src.services.user_service import add_or_update_user
from src.models.user import User


def test_save_user_message(db_session):

    user_id = 12345
    first_name = "Test"
    last_name = "User"
    username = "testuser"
    add_or_update_user(user_id, first_name, last_name, username, "en")

    user = db_session.query(User).filter_by(user_id=user_id).first()
    assert user is not None
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.username == "testuser"
