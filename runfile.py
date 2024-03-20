# username = input("What is your name")
# print(f"The User's name is {username}")
# if username == "Mercy":
#     print("Aaaah, kumbe ni wewe")
# else:
#     print(f"Alaah, who is this?")

from functionalities import functionalities
def main():
    while True:
        print("What do you want to do?")
        print("1. To see all teachers")
        print("2. To add a teacher")
        print("3. To find a teacher")
        print("4. Exit the application")
        userschoice = input("what do you want to do?")
        if userschoice == "1":
            # list all teachers
            list_teachers()
            input("Press Enter to continue")
        elif userschoice == "2":
            print("Functionality in implementation")
            input("Press Enter to continue")
        elif userschoice == "3":
            print("Functionality in implementation")
            input("Press Enter to continue")
        elif userschoice == "4":
            print("Exiting App, byee")
            return 0
        else:
            print("Invalid choice")
if  __name__ == '__main__':
    main()

