def check_password_strength(password):
    length = len(password)
    if length < 6:
        return "weak"
    elif length <= 10:
        if any(i.isalpha()for i in password) and any(i.isdigit() for i in password):
            return "strong"
        else:
            return "medium"
print(check_password_strength('abcd'))
