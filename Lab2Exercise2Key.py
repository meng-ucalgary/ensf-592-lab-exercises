# ENSF 592 Spring 2021
# May 11 Lab 2
# Exercise 2


# Trace through the execution of the following program. 
# Answer the questions in the comments with your group members.
# After discussing, use print statements to confirm your answers.

foo = 100
bar = foo
foo + bar

# POINT 1
# What is the value of foo at this point?
# What is the type of foo at this point?
# What is the value of bar at this point?
# What is the type of bar at this point?
print("***POINT 1***")
print("foo: ", foo, " Type: " + str(type(foo)))
print("bar: ", bar, " Type: " + str(type(bar)))

spam = foo + bar
foo += 50
eggs = foo + bar
ham = [1, 2, 3]
baz = ham
ham.append(bar)

# POINT 2
# What is the value of foo at this point?
# What is the value of bar at this point?
# What is the value of spam at this point?
# What is the value of eggs at this point?
# What is the value of ham at this point?
# What is the value of baz at this point?
print("***POINT 2***")
print("foo: ", foo, " Type: " + str(type(foo)))
print("bar: ", bar, " Type: " + str(type(bar)))
print("spam: ", spam, " Type: " + str(type(spam)))
print("eggs: ", eggs, " Type: " + str(type(eggs)))
print("ham: ", ham, " Type: " + str(type(ham)))
print("baz: ", baz, " Type: " + str(type(baz)))

eggs = "Python is very flexible!"
spam = ham   #  s, h, baz both ----->  [1, 2, 3, 100]
ham = bar   # ham to bar, s and baz ----> [1, 2, 3, 100]
bar += bar  # 100 + 100
foo = eggs
eggs = bar + ham
baz.append(bar)   # spam and baz ----->  [1, 2, 3, 100, 200]

# POINT 3
# What is the value of foo at this point?
# What is the value of bar at this point?
# What is the value of spam at this point?
# What is the value of eggs at this point?
# What is the value of ham at this point?
# What is the value of baz at this point?

# Print out the types and final values of each variable.
print("***POINT 3***")
print("foo: ", foo, " Type: " + str(type(foo)))
print("bar: ", bar, " Type: " + str(type(bar)))
print("spam: ", spam, " Type: " + str(type(spam)))
print("eggs: ", eggs, " Type: " + str(type(eggs)))
print("ham: ", ham, " Type: " + str(type(ham)))
print("baz: ", baz, " Type: " + str(type(baz)))

