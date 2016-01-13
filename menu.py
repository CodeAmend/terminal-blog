
class Menu(object):

    def __init__(self):
        self.user = input("What is the author name? ")
        if self._author_exists():
            print("does exists")
        else:
            self._add_new_blog()

    def _add_new_blog(self):
        print("adding new blog...")

    def _author_exists(self):
        return False

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
