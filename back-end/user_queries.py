from db import db
from models import User
 
# Create user from email and name and return the user object to the caller
def create_user(email: str, name: str) -> User:
    user = User(email=email, name=name)
    db.session.add(user)
    db.session.commit()
    return user

############################
# User retrieval functions #
############################

# retrieves the user by their id
def get_user_by_id(user_id: int) -> User | None:
    return User.query.get(user_id)

# retrieves the user by their email
def get_user_by_email(email: str) -> User | None:
    return User.query.filter_by(email=email).first()

# retrieves all users in the database
def get_all_users() -> list[User]:
    return User.query.all()

# retrieves all users whose name contains the given substring (case-insensitive)
def search_users_by_name(name_substring: str) -> list[User]:
    return User.query.filter(User.name.ilike(f"%{name_substring}%")).all()


###############################
# User modification functions #
###############################

# updates the user's name and returns the updated user object, or None if user not found
def update_user_name(user_id: int, new_name: str) -> User | None:
    # get user by their ID
    user = User.query.get(user_id)
    if not user:
        return None

    user.name = new_name # update the user's name
    db.session.commit() # commit the change to the database
    return user

# updates the user's email and returns the updated user object, or None if user not found
def update_user_email(user_id: int, new_email: str) -> User | None:
    # get user by their ID
    user = User.query.get(user_id)
    if not user:
        return None

    user.email = new_email # update the user's email
    db.session.commit() # commit the change to the database
    return user

# deletes the user by their ID and returns True if successful, False if user not found
def delete_user(user_id: int) -> bool:
    # get user by their ID
    user = User.query.get(user_id)
    if not user:
        return False

    db.session.delete(user) # deletes the user from the database
    db.session.commit() # commit the change to the database
    return True
