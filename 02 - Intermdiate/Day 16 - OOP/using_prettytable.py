from prettytable import PrettyTable

table = PrettyTable()  # Created object from PrettyTable Class

# add_column method take two input: First is fieldname and the other is the data we want to add to the column
table.add_column('City', ['Ankara', 'Istanbul', 'Malatya'])
table.add_column('Population', ['1.6M', '8.2M', '600K'])
print(table)


