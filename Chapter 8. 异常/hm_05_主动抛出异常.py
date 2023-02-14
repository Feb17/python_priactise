def validate_password(password):
    minimum_length = Exception("Minimum password length is 8")
    if len(password) < 8:
        raise minimum_length
    return password


try:
    pwd = input("Enter your password: ")
    print(validate_password(pwd))
except Exception as e:
    print(e)
