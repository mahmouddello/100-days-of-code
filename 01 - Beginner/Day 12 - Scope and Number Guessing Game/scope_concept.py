player_health = 10


# Local scope:

def drink_juice():
    juice = 'Orange juice'
    print(juice + "\n" + str(player_health))
    # When you create a new variable in a function (The variable should be indented)
    # it's (only) accessible from the function you can't use the variable outside the function


# Global Scope : The only difference between Global and Local Scope is where you did define your variable

drink_juice()

# Note : Indentations in if,while and for loop doesn't count as a local scope, and you can use the variables outside
# without problems like global variables because python doesn't have block scopes.
