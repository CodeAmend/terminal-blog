from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
<<<<<<< HEAD
        self.user = input("Enter your author name: ")
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._create_user_account()

    def _user_has_account(self):
        return Database.find_one('blogs', {"author":self.user}) is not None

    def _create_user_account(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        blog = Blog(self.user, title, description)
        blog.save_to_mongo()


    def run_menu(self):
        read_or_write = input("Do you want to read (R) or write (W)? ")
        if read_or_write == 'R':
=======
        self.user = input("Author name? ")
        if self._user_exists()
            print("Welcome to the dark side of the moon {}".format(self.user))
            Database.find('blogs', {"author": self.user})
        else:
            self._create_new_account()

    def _user_exists(self):
        return Database.find_one('blogs', {"author": self.user}) is not None

    #may be made static. Why?
    def _create_new_account(self):
        title = input("Title of the blog? ")
        description = input("Description of the blog? ")
        blog = Blog(self.user, title, description)
        # no need to create new_post() because we are essentially creating a new account.
        blog.save_to_mongo()

    def run_menu(self):
        read_or_write = input("Would you like to read (R) or write (W) a blog post? ")
        if read_or_write == "R":
>>>>>>> dude
            # list blogs in database
            # allow user to pick one
            # display posts
            pass
<<<<<<< HEAD
        if read_or_write == 'W':
            # check if user has blog
=======
        if read_or_write == "W":
            print("Read to write post...")

>>>>>>> dude
            # if yes promt to write a post
            # if not then promt to create a blog
            pass
        pass


