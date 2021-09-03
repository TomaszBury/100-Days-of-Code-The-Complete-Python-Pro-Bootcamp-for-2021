class User:
    def __init__(self, user_id, username):
        # initialise attributes
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("42", "E.T.")

print(user_1.username)

user_2 = User("002", "Jack")

print(user_2.username)
print(user_2.id)
print(user_2.followers)

# user_2.followers = 420
# print(user_2.followers)

user_1.follow(user_2)

print(f"user_1.followers: {user_1.followers}")
print(f"user_1.following: {user_1.following}")
print(f"user_2.followers: {user_2.followers}")
print(f"user_2.following: {user_2.following}")

