class Exercise_Sheet_1:

    def __init__(self):
        dummy = "n/a"

    def q1_1(self):
        # Exercise 1.1
        # Write the beer program again, counting down from 10 to 0 bottles, but for the special case of 6
        # bottles of beer, printing sixpack instead.
        # Use different looping methods:
        # 1. a while loop
        # 2. a for loop with the appropriate range function
        # and use the if condition appropriately.
        print("========================================")
        print("This is the for loop:")
        for i in range(10, -1, -1):
            if i == 6:
                print("A sixpack left.")
            else:
                print(i, "bottles of beer left.")
        print("========================================")
        print("This is the while loop")
        i = 10
        while i > -1:
            if i == 6:
                print("A sixpack left.")
            else:
                print(i, "bottles of beer left.")
            i -= 1

    def q1_2(self):
        # Exercise 1.2
        # Repeat Exercise 1.1 however in the regular case of i > 1, you are printing "bottles", while in the case of i=1, you would need to print "bottle".
        # Modify your previous program to use a variable plural which stores an "s" for the regular/plural case (i>1) and an empty string "" for the singular case (i=1) and generates the appropiate message for the two cases.
        print("========================================")
        print("This is the for loop:")
        for i in range(10, -1, -1):
            plural = "s"
            if i == 6:
                print("A sixpack left.")
                i-=1
            if i == 1:
                plural = ""
            print(i, " bottle" + plural + " of beer left.")

        print("========================================")
        print("This is the while loop")
        i = 10
        while i > -1:
            plural = "s"
            if i == 6:
                print("A sixpack left.")
                i -= 1
            if i == 1:
                plural = ""
            print(i, " bottle" + plural + " of beer left.")
            i-=1

    def q1_3(self):
        # Exercise 1.3
        # Do 1.1 again but using continue and break at the appropiate point in the program.
        print("========================================")
        print("This is the for loop:")
        for i in range(10, -1):
            if i < 0:
                break
            elif i == 6:
                print("A sixpack left.")
                i-=1
            else:
                print(i, "bottles of beer left.")
                continue



        # print("========================================")
        # print("This is the while loop")
        # i = 10
        # while i > -1:
        #     if i == 6:
        #         print("A sixpack left.")
        #     else:
        #         print(i, "bottles of beer left.")
        #     i -= 1

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

Exercise_Sheet_1().q1_3()