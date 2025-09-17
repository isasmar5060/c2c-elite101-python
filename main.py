
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""


def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")

def main():
    user_name = get_user_name()
    greet_user(user_name)

if __name__ == "__main__":
    main()


#adding my own rendition of the chatbot without the above functions
print("Welcome to the Walmart Chatbot!")
name = input("What is your name? ")
age = int(input("Hello " + name + ", how old are you in years? "))

if age < 9:
    print(str(age) + "? That's so cool!")
    print("To use the chatbot, I'd recommend that you get a parent to help first. See you later!")
else:
    query = input(str(age) + "? Great! Would you like an itemized list of my capabilities, " + name + "? (Y/N) ")

    if query.lower() == "y":
        print("Great! Here it is:")
        print("Press 1 for how to find your nearest Walmart store.")
        print("Press 2 to search for an item in the catalog.")
        print("Press 3 to report a damaged product in-store.")
        print("Press 4 for contact information for your selected store.")
        print("Press 5 to exit the chatbot.")

        choice = int(input("Please enter a number from 1 to 5."))
        if choice == 1:
            print("words words words")
        elif choice == 2:
            print("words words words 2")
        elif choice == 3:
            print ("words words words 3")
        elif choice == 4:
            print("words words words 4")
        elif choice == 5:
            print ("Thank you for talking to me, see you!")

    elif query.lower() == "n":
        print("Thank you for your participation! Exiting the program now.")
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
