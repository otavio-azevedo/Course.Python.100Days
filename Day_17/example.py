class User:
    # class constructor/initializer
    def __init__(self, user_id, username):
        # class attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self):
        print("=)")


user = User("001", "name")
user.follow()
print(user.name)
