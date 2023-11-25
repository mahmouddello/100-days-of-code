import json

# JSON: JavaScriptObjectNotation designed for JavaScript, but it got adopted by many filed including Python
# The structure of a JSON file looks like a Python Dictionary

############################
# Work with JSON in Python
############################
# import the built-in json module (imported in the top of the file)

################### - Methods - ###################

# json.dump() -> Write
# json.load() -> Read
# json.update() -> Update

# json.dump(new_data, dataFile, indent=4)  arg1: dictionary, arg2: file to write into, arg3: indentation = 4
# json.load(file_name)

# with open("data.json", mode="r") as dataFile:
# # Reading old data
# data = json.load(dataFile)
# # Updating old data with the new data
# data.update(new_data)
# except:
#
# with open("data.json", mode="w") as dataFile:
#     # Writing the new data
#     json.dump(data, dataFile, indent=4)
# clearing (wiping) the data in the website & password entries
#             website_entry.delete(0, tk.END)
#             password_entry.delete(0, tk.END)
