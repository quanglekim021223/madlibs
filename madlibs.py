
# This is a simple program to create a madlib. A madlib is a game where you fill in the blanks in a story with your own words to make a funny story.

# The user is asked to input an adjective
adj = input("Adjective: ")

# The user is asked to input a verb
verb1 = input ("Verb:")

# The user is asked to input another verb
verb2 = input ("Verb: ")

# The user is asked to input a famous person's name
famous_person = input("Famous person: ")

# A madlib is created using the f-string formatting in Python. The user's inputs are inserted into the madlib.
# The backslash at the end of the first line is used to continue the string onto the next line.
madlib = f"Computer programming is so {adj}! It makes me so excited all the time \
because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}! "

# The madlib is printed out
print(madlib)