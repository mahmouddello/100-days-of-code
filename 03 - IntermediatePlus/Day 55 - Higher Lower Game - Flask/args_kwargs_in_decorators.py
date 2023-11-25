class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = True


def is_authenticated(function):
    def wrapper(*args, **kwargs):
        # args[0], looks for the first positional argument passed by a function, hits inside the property
        # and checks if the user is logged in
        if args[0].is_logged_in:
            function(args[0])
        else:
            print("Not Authenticated")

    return wrapper


@is_authenticated
def create_blog_post(user: User):
    print(f"This is {user.name}'s new blog post!")


new_user = User("Mahmoud")
create_blog_post(new_user)
