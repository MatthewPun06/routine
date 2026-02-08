import bcrypt

# When creating a new user
def hash_password(plain_password): # Hash the password using bcrypt
    hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
    return hashed.decode('utf-8')  # Store this in the database

# When verifying a login
def check_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))