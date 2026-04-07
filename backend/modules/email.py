import re

def check_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    valid = re.match(pattern, email) is not None

    domain = email.split("@")[-1] if valid else None

    return {
        "email": email,
        "valid_format": valid,
        "domain": domain
    }
