class User:
    def __init__(self, user_id:int, name:str, age:int, gender:str, location:str, interests:list):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        self.profile = None

    def like(self, other_user):
        print(f"{self.name} liked {other_user.name}.")

    def message(self, other_user, message:str):
        print(f"{self.name} sent a message to {other_user.name}: {message}")