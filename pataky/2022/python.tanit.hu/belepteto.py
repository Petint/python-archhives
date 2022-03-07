class Users:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
    
    def login(self, max_tries: int = 5) -> bool:
        """Login prompt"""
        print("Login prompt V1")
        tries = 0
        while True:
            du_usernam = input("User: ")
            du_pass = input("Passord: ")
            if du_usernam == self.username and du_pass == self.password:
                print("Login successfull.")
                return True
            if tries >= max_tries - 1:
                print("Login failed.")
                return False
            tries += 1
            print(f"Wrong password and/or user name.\n You have {max_tries - tries} tries remaining.")


def register() -> Users:
    """Create new user"""
    _usr = input("Enter new Username: ")
    _pass = input("Enter new Password: ")
    return Users(_usr, _pass)


if __name__ == "__main__":
    petint = Users("Petint01", "Passw0rd")
    if petint.login():
        print("Works.")
