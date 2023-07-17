class Password:
    def __init__(self):
        self.siteName = None
        self.sitePassword = None

class PasswordBuilder:
    def __init__(self):
        self.password = Password()

    def set_siteName(self, name):
        self.password.siteName = name
        return self

    def set_sitePassword(self, password):
        self.password.sitePassword = password
        return self

    def build(self):
        return self.password
