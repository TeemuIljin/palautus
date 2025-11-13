import re

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def validate(self, username: str, password: str):
        """Validate username and password for new user registration.

        Rules:
        - username: only a-z, at least 3 chars, not already taken
        - password: at least 8 chars and not only letters
        """
        if not username or not password:
            raise UserInputError("Username and password are required")

        if len(username) < 3 or not re.match(r'^[a-z]+$', username):
            raise UserInputError("Invalid username")

        if len(password) < 8 or password.isalpha():
            raise UserInputError("Invalid password")

        # repository should expose find_by_username or similar
        existing = self._user_repository.find_by_username(username)
        if existing:
            raise UserInputError("Username already taken")

        return True