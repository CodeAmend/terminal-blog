from database import Database
from models.blog import Blog


class Menu(object):

    def __init__(self):
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
        # User read or write a blog?
        # if read:
            # list blogs in database
            # allow user to pick one
            # display posts
        # if write:
            # check if user has blog
            # if yes promt to write a post
            # if not then promt to create a blog
        pass
