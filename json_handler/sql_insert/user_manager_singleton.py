
# Singleton pattern implementation for managing user sessions.

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class UserManager(metaclass=SingletonMeta):    
    def __init__(self):
        self.current_user = None

    def login(self, user_id):        
        if self.current_user is None:
            self.current_user = user_id
            print(f"User {user_id} logged in successfully.")
            return True
        else:
            print("Another user is currently logged in. Please log out before attempting to log in a new user.")
            return False

    def logout(self):
        
        if self.current_user is not None:
            print(f"User {self.current_user} logged out successfully.")
            self.current_user = None
            return True
        else:
            print("No user is currently logged in.")
            return False

