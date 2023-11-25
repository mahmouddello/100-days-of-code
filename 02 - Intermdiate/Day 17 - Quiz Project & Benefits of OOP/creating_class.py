class User:
    pass
    # If we want temporarily to keep our class empty we should use the keyword 'pass' because python expect indentation


user1 = User()  # Initializing object from 'User Class'

user1.id = '001'  # id is an attribute
user1.username = 'Angela'  # username is an attribute

print(user1.username)  # Prints the username of the user1
