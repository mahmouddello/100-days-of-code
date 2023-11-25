# How to Open, Read and Write to a files using Python?

# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================

# Reading :
file = open("my_text.txt")
contents = file.read()
print(contents)
file.close()  # we need to close files to free resources of the computer when we're, or we just use (with) keyword
print("-" * 25)
# Using (with) keyword; if we forget to close the file, this keyword will close it automatically
with open("my_text.txt") as f:
    c = f.read()
    print(c)

# Writing:

with open("my_text.txt", mode='a') as x:
    x.write(f"We write to this file through Python Script")

# Creating a file from scratch (if the file name doesn't exist)

with open("new_file.txt", mode='w') as new_file:
    new_file.write("Created the file from scratch using Python :D")  # Done!
