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
        for i in range(10, -1, -1):
            if i < 0:
                break
            elif i == 6:
                print("A sixpack left.")
                continue
            else:
                print(i, "bottles of beer left.")
                continue

        print("========================================")
        print("This is the while loop")
        i = 10
        while True:
            if i < 0:
                break
            if i == 6:
                print("A sixpack left.")
            else:
                print(i, "bottles of beer left.")
            i -= 1
            continue

    def q1_4(self):
        # Exercise 1.4
        # Write the "beer" program again, but this time, make the printout line shorter at every decrement (ignore the last line for 0 bottles).
        mystring = "bottles of beer on the wall"

        print("========================================")
        print("This is the for loop:")
        x = 1
        for i in range(10, -1, -1):
            result_string = mystring[:-x]
            print(str(i) + " " + result_string)
            x += 1
        print("========================================")
        print("This is the while loop:")
        x = 1
        i = 10
        while i > -1:
            result_string = mystring[:-x]
            print(str(i) + " " + result_string)
            i-=1
            x += 1

    def q1_5(self):
        # Repeat Ecercise 1.4, but this time, starting the countdown from 40. What happens? and why?
        print("========================================")
        print("INCORRECT SOLUTION:")
        print("This is the for loop:")
        x = 1
        for i in range(40, -1, -1):
            result_string = str(i) + " bottles of beer on the wall"
            print(result_string[:-x])
            x += 1
        print("========================================")
        print("INCORRECT SOLUTION:")
        print("This is the while loop:")
        x = 1
        i = 40
        while i > -1:
            result_string = str(i) + " bottles of beer on the wall"
            print(result_string[:-x])
            i -= 1
            x += 1
        # Problem found was that 40 is too long so it completely erases the whole string including the bottle number!!

        # NOW THE SOLUTION. SEE BELOW CODE:
        mystring = "bottles of beer on the wall"
        print("========================================")
        print("CORRECT SOLUTION:")
        print("This is the for loop:")
        x = 1
        for i in range(40, -1, -1):
            result_string = mystring[:-x]
            print(str(i) + " " + result_string)
            x += 1
        print("========================================")
        print("CORRECT SOLUTION:")
        print("This is the while loop:")
        x = 1
        i = 40
        while i > -1:
            result_string = mystring[:-x]
            print(str(i) + " " + result_string)
            i -= 1
            x += 1

    def q1_6(self):
        mystring = "bottles of beer on the wall"
        print("========================================")
        print("This is the for loop:")
        x = 1
        for i in range(40, -1, -1):
            result_string = mystring[:-x]
            try:
                lastChar = result_string[-1]
                if lastChar == " ":
                    x += 1  # if space then skip it.
            except IndexError:
                x +=1

            print(str(i) + " " + result_string)
            x += 1

        print("========================================")
        print("This is the while loop:")
        x = 1
        i = 40
        while i > -1:
            result_string = mystring[:-x]
            try:
                lastChar = result_string[-1]
                if lastChar == " ":
                    x += 1  # if space then skip it.
            except IndexError:
                x += 1

            print(str(i) + " " + result_string)
            x += 1
            i -= 1

Exercise_Sheet_1().q1_6()