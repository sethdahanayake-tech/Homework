print("Homework Checker")

finished = "no"

while finished.lower() != "yes":
    finished = input("Have you finished your homework? (yes/no): ")

    if finished.lower() == "yes":
        print("Great job! You have finished your homework.")
    elif finished.lower() == "no":
        print("Keep working on your homework!")
    else:
        print("Please type 'yes' or 'no'.")

        