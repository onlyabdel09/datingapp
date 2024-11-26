class User:
    def __init__(self, user_id, name, age, gender, location, interests):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        self.profile = None

    def like(self, other_user):
        print(f"{self.name} liked {other_user.name}.")

    def message(self, other_user, message):
        print(f"{self.name} sent a message to {other_user.name}: {message}")


class Profile:
    def __init__(self, bio, photos, preferences):
        self.bio = bio
        self.photos = photos
        self.preferences = preferences

    def update_bio(self, new_bio):
        self.bio = new_bio
        print(f"Bio updated to: {new_bio}")

    def add_photo(self, photo_url):
        self.photos.append(photo_url)
        print(f"Photo added: {photo_url}")

    def set_preferences(self, preferences):
        self.preferences = preferences
        print(f"Preferences updated: {preferences}")


class Match:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.chat_history = []

    def send_message(self, sender, message):
        if sender in [self.user1, self.user2]:
            self.chat_history.append(f"{sender.name}: {message}")
            print(f"{sender.name} to Match: {message}")
        else:
            print("Sender is not part of this match.")

    def view_chat(self):
        print("Chat History:")
        for message in self.chat_history:
            print(message)


# Example Usage
if __name__ == "__main__":
    # Create Users
    user1 = User(1, "Alice", 25, "Female", "New York", ["Hiking", "Cooking"])
    user2 = User(2, "Bob", 28, "Male", "Los Angeles", ["Movies", "Running"])

    # Create Profiles
    profile1 = Profile("Love hiking and cooking!", ["alice_pic1.jpg"], {"age_range": (24, 30), "gender": "Male"})
    profile2 = Profile("Movies and outdoor adventures!", ["bob_pic1.jpg"], {"age_range": (22, 27), "gender": "Female"})

    # Assign Profiles to Users
    user1.profile = profile1
    user2.profile = profile2

    # Users Like Each Other
    user1.like(user2)
    user2.like(user1)

    # Match and Messaging
    match = Match(user1, user2)
    match.send_message(user1, "Hi Bob! Nice to meet you.")
    match.send_message(user2, "Hi Alice! Great to meet you too.")
    match.view_chat()
