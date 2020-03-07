import hashlib
import pickle

class AuthException(Exception):
    def __init__(self, username, user=None):
        super().__init__(username, user)
        self.username = username
        self.user = user

class UserExists(AuthException):
    pass

class PasswordtooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPass(AuthException):
    pass

class NotloggedIn(AuthException):
    pass

class User:
    def __init__(self, user, password):
        self.user = user
        self.password = self.encrypt_pass(password)
        self.already_logged_in = False

    def encrypt_pass(self, password):
        string_to_encrypt = self. user + password
        encrypted_pass = string_to_encrypt.encode("utf8")
        return hashlib.sha256(encrypted_pass).hexdigest()

    def check_paswrd(self, check_string):
        return self.password == self.encrypt_pass(check_string)


class Authenticate:
    def __init__(self):
        self.users = {}

    def add_user(self, user, password):
        if user in self.users:
            raise UserExists(user)
        if len(password) < 6:
            raise PasswordtooShort(user)

        self.users[user] = User(user, password)

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_paswrd(password):
            raise InvalidPass(username, password)
        user.already_logged_in = True
        return True

    def save_users(self):
        try:
            output = open(("users.pkl"), 'wb')
        except AttributeError:
            print("No new users to update")
        else:
            pickle.dump(self.users, output, pickle.HIGHEST_PROTOCOL)

    def load_users(self):
        try:
            input = open(("users.pkl"), 'rb')
        except FileNotFoundError:
            print("There is no stored users!")
        else:
            print("Previous session loaded")
            obj = pickle.load(input)
            input.close()
            print("Load complete")
            self.users = obj


auth = Authenticate()
