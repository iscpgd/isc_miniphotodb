import pages
import database
import os


def username_validation(username):
    # validate username > 10 and no whitespace
    if ' ' in username or len(username) > 10:
        print("invalid username")
        print("should not contain spaces or greater than 10 characters")
        return False
    else:
        return True


def password_validation(input_password):
    # validate password make sure at least 10 characters long no whitespace
    if ' ' in input_password or len(input_password) < 10:
        print("invalid password")
        print(
            "password should not contain spaces and need to be greater than 10 characters")
        return False
    else:
        return True


def path_validation(path):
    # validation for both path and file existence
    if os.path.exists(path):
        return True
    else:
        print("path does not exist. try again")
        return False


def image_validation(path):
    # validation for photo file format existence
    image_format = ["jpg", "png", "tif", "bmp"]
    if os.path.exists(path) and path[-3:] in image_format:
        return True
    else:
        print("path does not exist or invalid file format dude. try again")
        return False


def options_validation(valid_list, input):
    if input not in valid_list:
        print("sorry that is not an option")
        return False
    else:
        # remove soon
        return True
