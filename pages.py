# valid list is for validation of all inputs within the page

# have a dictionary of all options and the corresponding function to use
import database as d


def welcome_page():
    valid_list = ["s", "l", "q"]
    print("*"*7 + "WELCOME TO THE ONE-PHOTO STORAGE HOUSE" + "*"*7)
    print("-----select one of the following-----")
    print(" s - sign up")
    print(" l - log in")
    print(" q - quit")
    return valid_list


def signup_page():
    valid_list = ["s", "h", "q"]
    print("*"*7 + "THANKS FOR SIGNING UP" + "*"*7)
    print(" s - sign up now")
    print(" h - home")
    print(" q - quit")
    return valid_list


def login_page():
    valid_list = ["h", "q", "l"]
    print("*"*7 + "YOU ARE NOW IN THE LOG IN PAGE BRUH!" + "*"*7)
    print(" l - log in now")
    print(" h - home")
    print(" q - quit")
    return valid_list


def locker_page(photo_exists):
    valid_list_exist = ["o", "r", "l"]
    valid_list_notexist = ["a", "l"]
    print("*"*7 + "YOU ARE IN YOUR LOCKER" + "*"*7)
    print("-----select one of the following-----")
    if photo_exists:
        print(" o - open photo")
        print(" r - remove photo")
        print(" l - logout")
        return valid_list_exist
    else:
        print(" a - add photo")
        print(" l - logout")
        return valid_list_notexist
