# Imagine you want to save the U.S. states to use it in your program somewhere
# instead of creating a single variable for evrey single state we can concatenate them in a list data structures
# List : is a data structure to store the information and can contain different data types.

states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                     "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
                     "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                     "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
                     "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                     "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                     "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
print(states_of_america[0])  # Alabama
# We can use a negative index too
print(states_of_america[-1])  # Wyoming
# Negative index will start counting from the end and index [-1] represent the last item on that list

# We can also add a new item to the end of the list by using append() function

states_of_america.append("New City")

print(states_of_america)