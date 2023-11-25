# In computer programming,
# a file or directory path specifies the location of a file or directory in a file system.
# There are two types of paths: absolute paths and relative paths.
#
# An absolute path is a complete path that specifies the exact location of a file or directory in a file system,
# starting from the root directory.
# It includes all the directories and subdirectories necessary to locate the file or directory.
# For example, /home/user/documents/file.txt is an absolute path.


# A relative path is a path that specifies the location of a file or directory relative to the current
# working directory of the program. It does not include the root directory and starts with a directory name
# or a . Or .. notation. For example,
# documents/file.txt is a relative path if the current working directory is /home/user/.

# Let's open a text file through an absolute path

with open("C:/Users/Zeus/Desktop/Data Science/desktop_file.txt", mode='r') as file:
    contents = file.read()
    print(contents)

print("-" * 25)
# Let's open a text file through a relative path
with open("./my_text.txt", mode='r') as file2:
    contents = file2.read()
    print(contents)
