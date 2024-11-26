from user import User
from match import Match
from profile import Profile

if __name__ == "__main__":
    user1 = User(1, "Alice", 25, "Female", "New York", ["Hiking", "Cooking"])
    user2 = User(2, "Bob", 28, "Male", "Los Angeles", ["Movies", "Running"])

    profile1 = Profile("Love hiking and cooking!", ["alice_pic1.jpg"], {"age_range": (24, 30), "gender": "Male"})
    profile2 = Profile("Movies and outdoor adventures!", ["bob_pic1.jpg"], {"age_range": (22, 27), "gender": "Female"})

    user1.profile = profile1
    user2.profile = profile2

    user1.like(user2)
    user2.like(user1)

    match = Match(user1, user2)
    match.send_message(user1, "Hi Bob! Nice to meet you.")
    match.send_message(user2, "Hi Alice! Great to meet you too.")
    match.view_chat()
