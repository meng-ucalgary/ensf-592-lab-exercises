
### Review of else statement in loops (Lesson 6)

L = []  # new list
nmax = 30 # max we're going up to 30

# iterate from 2 up to 30
for n in range(2, nmax):    # 2 to 30

    # iterate over each value in the current form of list
    for factor in L:
        # if this is true, break the loop!
        if n % factor == 0:
            print("Loop broke early")
            break
        print("Loop finished naturally")

    # only execute this code IF the nested loop DIDN'T break (finished naturally without encountering a break)
    else: # no break
        print("RUN!")
        L.append(n)  # Adds to L if the inner loop finished all iterations without breaking


print(L)  # happens when all else is done!