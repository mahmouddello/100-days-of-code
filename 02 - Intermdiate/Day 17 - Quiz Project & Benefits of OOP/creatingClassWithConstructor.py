class User:
    def __init__(self, user_id, user_name):
        # initialise attributes whenever we create a new object
        print('Creating a new user...')  # when we create a new object this print statement will be triggered
        self.id = user_id
        self.user_name = user_name
        self.followers = 0  # Default value. Explained in Notes file Section 5.4


user1 = User(1, 'Angela')
print(f'{user1.id}, {user1.user_name}')
user2 = User(2, 'Mahmoud')
print(f'{user2.id}, {user2.user_name}')

# When we're creating a new object with specified parameters, we can't let the argument empty, or we got an error.
# Example : user3 = User(3) >>
# This will cause an error because  we didn't pass any (argument) to set in place of the username (parameter).


