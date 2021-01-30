import sqlite3
import base64
import imageio
import cv2
import os

# create a database in the project folder call photo.db
conn = sqlite3.connect('photo.db')

# database structure will be simple username password and the decoded img!
c = conn.cursor()
c.execute('''CREATE TABLE if not exists photo
             (username text unique,
             password text,
             image text)'''
          )
conn.commit()


def add_user(username, password):
    # add user to the database
    try:
        c.execute("INSERT INTO photo VALUES(?,?,?)",
                  (username, password, None,))
        conn.commit()
        print(f"username added: {username}")
    except:
        print("error: username already exists")


def remove_user(username):
    # remove the user from the database
    c.execute("DELETE FROM photo WHERE username = ?", (username,))
    conn.commit()
    print(f"username deleted: {username}")


def add_photo(photopath, username):
    # add a photo to a corresponding users locker
    image = cv2.imread(photopath)
    string_image = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
    print(string_image)
    c.execute("UPDATE photo SET image = ? where username = ?",
              (string_image, username,))
    conn.commit()
    print("photo added to database!")


def remove_photo(username):
    # remove a photo from a corresponding users locker
    c.execute("UPDATE photo SET image = ? where username = ?",
              (None, username,))
    conn.commit()
    print("photo removed!")


def open_photo(username, outputpath):
    # export the photo out of the database so user can open it/access it
    os.path.isdir(outputpath)
    c.execute("SELECT image from photo where username = ?", (username,))
    image_string = (c.fetchone()[0])
    print("copy of photo exported from database!")
    image = base64.b64decode(image_string)
    filename = os.path.join(outputpath, "image.jpg")
    with open(filename, 'wb') as file:
        file.write(image)


def check_photo_exists(username):
    # check if a user has a photo or no
    c.execute("SELECT image from photo where username = ?", (username,))
    return c.fetchone()[0] is not None


def check_usernamepassword(username, password):
    # validate password make sure it is right you know?
    c.execute("SELECT password from photo where username = ?", (username,))
    if c.fetchone() is not None:
        c.execute("SELECT password from photo where username = ?", (username,))
        if password == c.fetchone()[0]:
            return True
        else:
            print("invalid username and password. please try again.")
            return False
    else:
        print("that username doesnt exist... i think.. try again")


def count_rows():
    # for development use
    for row in c.execute('SELECT * from photo'):
        print(row)


def delete_table():
    # for development use
    c.execute("DROP table photo")
    print("table dropped!")
    conn.commit()
