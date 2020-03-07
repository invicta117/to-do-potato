import loginbackend
import todoprogram

class Interface:
    def __init__(self):
        self.options = {"1": self.login, "3": self.exit, "2": self.add_user}
        self.quit = False

    def login(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        try:
            loginbackend.auth.login(username, password)
        except loginbackend.InvalidUsername:
            print("This is not a valid username!")
        except loginbackend.InvalidPass:
            print("This is not a valid password")
        else:
            print("You have been logged in sucessfully!")
            m = todoprogram.Menu()
            m.run(username)


    def exit(self):
        self.save()
        self.quit = True

    def menu(self):
        print(
            """
            1. login
            2. add new user
            3. quit
            """
        )

    def run(self):
        self.load()
        while not self.quit:
            self.menu()
            ip = input("Enter menu command: ")
            action = self.options.get(ip)
            if action:
                action()
            else:
                print("Please enter a valid option")

    def add_user(self):
        username = input("Please enter your new username: ")
        password = input("Please enter your new password: ")
        try:
            loginbackend.auth.add_user(username, password)
        except loginbackend.PasswordtooShort:
            print("Passowrd must be longer than 6 characters!")
        except loginbackend.UserExists:
            print("This username is taken!")


    def load(self):
        loginbackend.auth.load_users()

    def save(self):
        loginbackend.auth.save_users()

if __name__ == "__main__":
    I = Interface()
    I.run()


