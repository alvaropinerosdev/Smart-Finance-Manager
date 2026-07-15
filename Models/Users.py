class User:
    def __init__(self,userId, username, firstName, lastName, email, password_hash, createdAt):
        self.userId = userId
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password_hash = password_hash
        self.createdAt = createdAt

    def register(self):
        # Code to register the user in the database
        pass

    def login(self):
        # Code to authenticate the user
        pass

    def updateProfile(self, firstName=None, lastName=None, email=None):
        # Code to update the user's profile information
        if firstName:
            self.firstName = firstName
        if lastName:
            self.lastName = lastName
        if email:
            self.email = email
        # Update the database with the new information
        pass
    
    def logout(self):
        # Code to log the user out
        pass

    


    