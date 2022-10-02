import bcrypt


def hash_pswd(password: str):
    salt = bcrypt.gensalt(14)
    # print({"salt": salt})
    hashpw = bcrypt.hashpw(str(password).encode('utf-8'), salt)
    return hashpw.decode()

def change_password(modelInstance, password: str):
    # modelInstance.password = hash_pswd(str(modelInstance.password))
    modelInstance.password = hash_pswd(password)
    # super().save()
    modelInstance.save()