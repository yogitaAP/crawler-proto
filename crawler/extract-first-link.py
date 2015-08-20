# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.
# Your code should print http://udacity.com
# Make sure that if page were changed to
# page = '<a href="http://udacity.com">Hello world</a>'
# that your code still prints the same thing.

# page = contents of a web page
page =('<a href="http://udacity.com">Hello world</a>')
start_link = page.find('<a href=')
start_index = page.find("\"", start_link)
stop_index = page.find("\">", start_link)
url = page[start_index+1:stop_index]
print url
