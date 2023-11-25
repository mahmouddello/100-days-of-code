# REST : Representational State Transfer
# Client sends a -> (HTTP Request) to the server, HTTPS stands for HTTPSecure Request
# there is also Ftp -> File Transfer Protocol

"""
how to make api RESTful?
1) Using HTTP requests verbs; GET, POST, PUT, PATCH(*NEW), DELETE.
2) Specific pattern of routes
"""

"""When returning an api response:
1) The method described in the docs has maximum flexibility. It allows you to have perfect control over 
the JSON response. e.g. You could also structure the response by omitting some properties like id. 
You could also group the Boolean properties into a subsection called "amenities".
2) But in most cases, you might just want to return all the data you have on a particular record and it would drive you 
crazy if you had to write out all that code for every route.
So another method of serialising our database row Object to JSON is by first converting it to a dictionary and then 
using jsonify() to convert the dictionary (which is very similar in structure to JSON) to a JSON.
[main.py to_dict function]
"""
