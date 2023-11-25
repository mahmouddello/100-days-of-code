class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    # method
    def follow(self, user):
        user.followers += 1  # ازا حدا تابع يوزر معين عداد المتابعين عنده بزيد
        self.following += 1  # ازا يوزر تابع يوزر اخر يزيد عداد العالم اللي متابعها عنده


user1 = User(1, 'Angela')
user2 = User(2, 'Mahmoud')

user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)
