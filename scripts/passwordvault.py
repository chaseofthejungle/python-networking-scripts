import string
import secrets

def generate_password(length=14):
    chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(secrets.choice(chars) for i in range(length))
    return password

# Store secure pass through hashing and then placing pass in a file or db
def store_password(service, username, password):
    hashed_password = hash_function(password)

    with open("pass_data.txt", "a") as f:
        f.write(f"{service},{username},{hashed_password}\n")

# Pass lookup in a file or db, comparing stored pass and provided pass
def get_password(service, username):
    with open("pass_data.txt") as f:
        for line in f:
            service_, username_, hashed_password_ = line.strip().split(",")
            if service == service_ and username == username_:
                if hash_function(password) == hashed_password_:
                    return password
        return None
