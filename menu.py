from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
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
        author = input("What is the author name? ")
        title = input("Title of the blog? ")
        description = input("Description of the blog? ")
        blog = Blog(author, title, description)
        blog.new_post()
        blog.save_to_mongo()

    def run_menu(self):
        read_or_write = input("Would you like to read (R) or write (W) a blog post? ")
        if read_or_write == "R":
            # list blogs in database
            # allow user to pick one
            # display posts
            pass
        if read_or_write == "W":
            print("Read to write post...")

            # if yes promt to write a post
            # if not then promt to create a blog
            pass
        pass


