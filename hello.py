# Get user name for greeting
name = input("What's your name? ").strip().title()

# Remove whitespace from string AND capitalize user's name
# name = name.strip().title()
#   ^ Don't even NEED this, you can add these methods
#       to the string

# Capitalize user name
# name = name.capitalize()

# Capitalizes first character of each word
# name = name.title()

# Greet the  user
print("hello, " + name) # The traditional way of printing

# Another way of printing name:
# print("hello,", name)
#   ^ This uses a hidden named parameter of python
#       where name is another argument to be added
#       and separated with a space

# Another format:
# print("hello, ", end='')
# print(name)
#   ^ this format takes advantage of the named parameters
#       in the print() function

# Here's another way:
# print(f"hello, {name}")
#   ^ This uses a new way, where f denotes special formatting
#       for the string, thus allowing name to be enclosed
#       in braces