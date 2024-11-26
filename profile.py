class Profile:
    def __init__(self, bio:str, photos:list, preferences:list):
        self.bio = bio
        self.photos = photos
        self.preferences = preferences

    def update_bio(self, new_bio:str):
        self.bio = new_bio
        print(f"Bio updated to: {new_bio}")

    def add_photo(self, photo_url:str):
        self.photos.append(photo_url)
        print(f"Photo added: {photo_url}")

    def set_preferences(self, preferences:list):
        self.preferences = preferences
        print(f"Preferences updated: {preferences}")