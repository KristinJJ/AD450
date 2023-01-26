# Kristin Jue
# AD450 Winter 2023
# Week 4, Calculate GPA

# ask the user if they would like to calculate GPA
print("Would you like to calculate a GPA? Y/N")
answer = input()

if answer == "Y":
    # initialize the GPA
    gpa = 0.0
  
    while answer == "Y":
        print('Enter a percent as a floating value (e.g. 87% would be entered as 87.0):')
    
        # take in the percent value
        percent = float(input())
    
        # calculate GPA
        if percent < 100.0 and percent >= 95.0:
            gpa = 4.0
        elif percent < 95.0 and percent >= 94.0:
            gpa = 3.9
        elif percent < 94.0 and percent >= 93.0:
            gpa = 3.8
        elif percent < 93.0 and percent >= 92.0:
            gpa = 3.7
        elif percent < 92.0 and percent >= 91.0:
            gpa = 3.6
        elif percent < 91.0 and percent >= 90.0:
            gpa = 3.5
        elif percent < 90.0 and percent >= 89.0:
            gpa = 3.4
        elif percent < 89.0 and percent >= 88.0:
            gpa = 3.3
        elif percent < 88.0 and percent >= 87.0:
            gpa = 3.2
        elif percent < 87.0 and percent >= 86.0:
            gpa = 3.1
        elif percent < 86.0 and percent >= 85.0:
            gpa = 3.0
        elif percent < 85.0 and percent >= 84.0:
            gpa = 2.9
        elif percent < 84.0 and percent >= 83.0:
            gpa = 2.8
        elif percent < 83.0 and percent >= 82.0:
            gpa = 2.7
        elif percent < 82.0 and percent >= 81.0:
            gpa = 2.6
        elif percent < 81.0 and percent >= 80.0:
            gpa = 2.5
        elif percent < 80.0 and percent >= 79.0:
            gpa = 2.4
        elif percent < 79.0 and percent >= 78.0:
            gpa = 2.3
        elif percent < 78.0 and percent >= 77.0:
            gpa = 2.2
        elif percent < 77.0 and percent >= 76.0:
            gpa = 2.1
        elif percent < 76.0 and percent >= 75.0:
            gpa = 2.0
        elif percent < 75.0 and percent >= 74.0:
            gpa = 1.9
        elif percent < 74.0 and percent >= 73.0:
            gpa = 1.8
        elif percent < 73.0 and percent >= 72.0:
            gpa = 1.7
        elif percent < 72.0 and percent >= 71.0:
            gpa = 1.6
        elif percent < 71.0 and percent >= 70.0:
            gpa = 1.5
        elif percent < 70.0 and percent >= 69.0:
            gpa = 1.4
        elif percent < 69.0 and percent >= 68.0:
            gpa = 1.3
        elif percent < 68.0 and percent >= 67.0:
            gpa = 1.2
        elif percent < 67.0 and percent >= 66.0:
            gpa = 1.1
        elif percent < 66.0 and percent >= 65.0:
            gpa = 1.0
        elif percent < 65.0 and percent >= 0.0:
            gpa = 0.0
    
        # prints out the GPA
        print('GPA is: ' + str(gpa))
    
        # asks user if they would like to continue
        print("Would you like to calculate another GPA? Y/N")
        answer = input()
    
        # say goodbye
        if (answer == "N"):
            print("Goodbye!")
    
# say goodbye
else:
    print("Goodbye!")

