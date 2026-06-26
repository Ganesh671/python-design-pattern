class AuthHandler:
    instance = None

    def __init__(self):
        self.isLoggedIn = False
    
    @staticmethod
    def getAppState():
        if not AuthHandler.instance:
            AuthHandler.instance = AuthHandler()
        
        return AuthHandler.instance

auth = AuthHandler.getAppState()
print(auth.isLoggedIn)
auth2 = AuthHandler.getAppState()
auth.isLoggedIn = True
auth3 = AuthHandler.getAppState()
print(auth3.isLoggedIn)
print(auth2.isLoggedIn)