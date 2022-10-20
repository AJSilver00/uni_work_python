# Write the beer program again, counting down from 10 to 0 bottles, but for the special case of 6
# bottles of beer, printing sixpack instead.
# Use different looping methods:
# 1. a while loop
# 2. a for loop with the appropriate range function
# and use the if condition appropriately.


class Exercise_Sheet_1:

    def __init__(self):
        dummy = "n/a"

    def q1_1(self, i):
        print("========================================")
        print("This is the for loop:")
        print(i, " bottles of beer.")
        i -= 1
        for x in range(i, 1, -1):
            if x == 6:
                print("A sixpack left.")
            else:
                print(x, "bottles of beer left.")
        print("1 bottle of beer left.")
        print("No more bottles of beer left!")
        print("========================================")
        print("This is the while loop")
        print(i, "bottles of beer.")
        i -= 1
        while i > 1:
            if i == 6:
                print("A sixpack left.")
            else:
                print(i, "bottles of beer left.")
            i -= 1
        print("1 bottle of beer left.")
        print("No more bottles of beer left!")

    def q1_2(self, i):
        print("========================================")
        print("This is the for loop:")
        i=10
        plural = "s"
        for x in range(i, 0, -1):
            if x == 1: plural = ""
            print(x, " bottle" + plural + " of beer left.")
        print("No more bottles of beer left!")
        print("========================================")
        print("This is the while loop:")
        plural = "s"
        while i > 0:
            if i == 1: plural = ""
            print(i, " bottle" + plural + " of beer left.")
            i -= 1
        print("No more bottles of beer left!")

    def q1_3(self, i):
        print("========================================")
        print("This is the for loop:")
        for x in range(i, 1, -1):
            if x == 6: print("A sixpack left.")
            else: print(x, "bottles of beer left.")
        print("1 bottle of beer left.")
        print("No more bottles of beer left!")

        print("========================================")
        print("This is the while loop")
        top = i
        plural = "s"
        while i > 0:
            if i == top: print(i, "bottles of beer.")
            elif i == 6: print("A sixpack left.")
            elif i == 1: print("1 bottle of beer left."); break
            else: print(i, "bottles of beer left.")
            i-=1
        print("No more bottles of beer left!")

    def q1_4(self, i):
        print("========================================")
        print("This is the for loop:")

        print("========================================")
        print("This is the while loop:")

    def q1_5(self, i):
        print("========================================")
        print("This is the for loop:")

        print("========================================")
        print("This is the while loop:")

    def q1_(self, i):
        print("========================================")
        print("This is the for loop:")

        print("========================================")
        print("This is the while loop:")

Exercise_Sheet_1().q1_3(10)