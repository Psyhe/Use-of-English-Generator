from scraper import get_bbc_text
from use_of_english import prepare_task

def input_number():
    try:
        choice = int(input("Enter the number of the operation: "))
        if choice < 1 or choice > 3:
            print("Invalid input. Please enter a number between 1 and 3.")
            return input_number()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return input_number()

    return choice

def what_you_want_menu():
    print("What do you want to do?")
    print("1. Get a text from BBC")
    print("2. Prepare a Use of English task")
    print("3. Quit")
    answer = input_number()

    if answer == 1:
        url = input("Enter the URL of the article: ")
        get_bbc_text(url)
    elif answer == 2:
        prepare_task()

if __name__ == "__main__":
    what_you_want_menu()