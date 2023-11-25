enemy = 1


# Modifying a global variable in a local scope which is the increase function
def increase():
    global enemy  # We can modify a global variable inside a local space by using 'global' keyword
    enemy += 1
    print(f"Enemy inside {enemy}")


increase()
print(f"Enemy Outside {enemy}")
