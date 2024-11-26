from user import User

class Match:
    def __init__(self, user1:User, user2:User):
        self.user1 = user1
        self.user2 = user2
        self.chat_history = []

    def send_message(self, sender:User, message:str):
        if sender in [self.user1, self.user2]:
            self.chat_history.append(f"{sender.name}: {message}")
            print(f"{sender.name} to Match: {message}")
        else:
            print("Sender is not part of this match.")

    def view_chat(self):
        print("Chat History:")
        for message in self.chat_history:
            print(message)