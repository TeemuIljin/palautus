from dataclasses import dataclass
import re
import sys

class UserInputError(Exception):
    pass

class AuthenticationError(Exception):
    pass

@dataclass
class User:
    username: str
    password: str

class UserRepository:
    def __init__(self):
        self._users = []

    def find_by_username(self, username: str):
        for u in self._users:
            if u.username == username:
                return u
        return None

    def create(self, user: User):
        self._users.append(user)
        return user

class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def validate(self, username: str, password: str):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3 or not re.fullmatch(r"[a-z]+", username):
            raise UserInputError("Invalid username")

        if len(password) < 8 or password.isalpha():
            raise UserInputError("Invalid password")

        if self._user_repository.find_by_username(username):
            raise UserInputError("Username already taken")

        return True

    def create_user(self, username: str, password: str):
        self.validate(username, password)
        user = User(username=username, password=password)
        return self._user_repository.create(user)

    def check_credentials(self, username: str, password: str):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)
        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")
        return user

def main():
    repo = UserRepository()
    svc = UserService(repo)

    # Read all lines from stdin until EOF and process sequentially
    inputs = []
    for line in sys.stdin:
        inputs.append(line.rstrip("\n"))

    idx = 0
    while idx < len(inputs):
        cmd = inputs[idx].strip()
        idx += 1
        if not cmd:
            continue

        if cmd == "new":
            # expect username then password
            if idx + 1 > len(inputs):
                print("Missing username/password")
                break
            username = inputs[idx].strip() if idx < len(inputs) else ""
            idx += 1
            password = inputs[idx].strip() if idx < len(inputs) else ""
            idx += 1
            try:
                svc.create_user(username, password)
                print("User created")
            except UserInputError as e:
                print(str(e))
            continue

        if cmd == "login":
            # expect username then password
            if idx + 1 > len(inputs):
                print("Missing username/password")
                break
            username = inputs[idx].strip() if idx < len(inputs) else ""
            idx += 1
            password = inputs[idx].strip() if idx < len(inputs) else ""
            idx += 1
            try:
                svc.check_credentials(username, password)
                print("Logged in")
            except (UserInputError, AuthenticationError):
                print("Invalid username or password")
            continue

        # ignore other commands
    # end while

if __name__ == "__main__":
    main()