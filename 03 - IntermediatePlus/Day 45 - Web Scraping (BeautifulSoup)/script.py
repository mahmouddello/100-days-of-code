from bs4 import BeautifulSoup

with open("website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# passing string of contents to the markup, parser we can pass html or xml sometimes we should use 'lxml'

print(soup.prettify())
print("-" * 50)
print(soup.title)  # gets the title tag and the string
print(soup.title.name)  # gets the "tag" name
print(soup.title.string)  # gets the string inside the title tag
print("-" * 50)

print(soup.a)  # prints the first anchor tag
print(soup.li)  # prints the first list element
print(soup.p)  # prints the first paragraph element
print("-" * 50)

# findAll() : finds all elements of the specified tag
all_anchor_tags = soup.findAll('a')  # find all anchor tags, type (list)
print(all_anchor_tags)

# Get all text in each anchor tag
for tag in all_anchor_tags:
    print(tag.getText())

# Get all links in each anchor tag
for tag in all_anchor_tags:
    print(tag.get("href"))
print("-" * 50)

# find by the tag and id of the element
print(soup.find(name="h1", id="name"))

# find by the tag and class name of the element
section_heading = soup.find(name="h3", class_="heading")  # "class_" is not the same as "class"
print(section_heading.string)
print("-" * 50)

# We can also use the CSS Selectors

# Selects only one result (id already unique but watch out for classes)
name = soup.select_one(selector="#name")
print(name)

# to select all elements that have class name "heading"
headings = soup.select(selector=".heading")
print(headings)  # list
