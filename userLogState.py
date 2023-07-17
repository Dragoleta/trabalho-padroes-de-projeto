from logState import LogState


class LoggedOutState(LogState):
    def login(self, manager, username):
        print("Logging in...")
        manager.set_user(username)
        manager.set_state(LoggedInState())

    def logout(self):
        print("Logging out...")


class LoggedInState(LogState):
    def login(self, username):
        print("You are already logged in.")

    def logout(self, manager):
        print("Logging out...")
        manager.set_user(None)
        manager.set_state(LoggedOutState())


class LogManager:
    def __init__(self):
        self.state = LoggedOutState()
        self.user = None

    def login(self, username):
        self.state.login(self, username)

    def logout(self):
        self.state.logout(self)

    def set_user(self, user):
        self.user = user

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_user(self):
        return self.user
