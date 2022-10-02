import bcrypt


def verify_pswd(password: str, hashed_password: str):
    _password = bytes(password, 'UTF-8')
    _hashed_password = bytes(hashed_password, 'UTF-8')
    # print({"qS...password": password})
    return bcrypt.checkpw(_password, _hashed_password)