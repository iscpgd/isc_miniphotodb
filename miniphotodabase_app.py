import database as d
import pages as p
import input_validation as iv

open = True


def input_intro(page):
    # this validates all the user inputs by letter codes
    while True:
        input_intro = input("enter input here: ")
        if iv.options_validation(page, input_intro):
            return input_intro


def app_welcome():
    global open
    input_act = input_intro(p.welcome_page())
    if input_act == "s":
        app_signup_func(input_act)
    elif input_act == "l":
        app_login_func(input_act)
    elif input_act == "q":
        open = False


def app_signup_func(input_enduser):
    # we are in the signup page. what to do in the sign up page
    global open
    x = True
    while x:
        input_act = input_intro(p.signup_page())
        if input_act == "s":
            while True:
                input_uname = input("input username here: ")
                if iv.username_validation(input_uname):
                    break
            while True:
                input_upw = input("input password: ")
                if iv.password_validation(input_upw):
                    break
            d.add_user(input_uname, input_upw)
            x = False
        elif input_act == "h":
            return False
        elif input_act == "q":
            open = False
            break


def app_locker_func(username):
    # we are in the locker page. what to do in the locker page
    global open
    x = True
    while x:
        photo_exists = d.check_photo_exists(username)
        if photo_exists:
            input_act = input_intro(p.locker_page(True))
            if input_act == "o":
                while True:
                    input_outputpath = input(
                        "enter file path here so we can export it there: ")
                    if iv.path_validation(input_outputpath):
                        break
                d.open_photo(username, input_outputpath)
            elif input_act == "r":
                d.remove_photo(username)
            elif input_act == "h":
                x = False
            elif input_act == "q":
                open = False
                break
        else:
            input_act = input_intro(p.locker_page(False))
            if input_act == "a":
                while True:
                    input_importpath = input(
                        "enter full path of the photo here so we can import it (NOTE: only jpg, png, bmp, tif pls): ")
                    if iv.image_validation(input_importpath):
                        break
                d.add_photo(input_importpath, username)
            elif input_act == "l":
                x = False


def app_login_func(input_enduser):
    # we are in the login page. what to do in the login page
    global open
    x = True
    while x:
        input_act = input_intro(p.login_page())
        if input_act == "l":
            while True:
                input_uname = input(
                    "what is your username (press h to go back home)? ")
                if input_uname == "h":
                    return True
                input_upw = input(
                    "what is your password(press h to go back home)?  ")
                if input_upw == "h":
                    return True
                elif d.check_usernamepassword(input_uname, input_upw):
                    break
            app_locker_func(input_uname)
        elif input_act == "h":
            x = False
        elif input_act == "q":
            open = False
            break


def main():
    while open:
        app_welcome()


if __name__ == "__main__":
    main()
