def quiz_user(quiz_file):
    success = 0
    with open(quiz_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.split("? ")
            print(parts[0] + "?")
            if input("> ").lower() == parts[1].lower():
                print("Correct!")
                success += 1
            else:
                print("Incorrect! You probably meant " + parts[1])
    return success

quiz_user("testQuiz.txt")