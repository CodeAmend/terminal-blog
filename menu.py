from database import Database
from models.blog import Blog
from models.post import Post


class Menu(object):

    def __init__(self):
        self.user = input("Author name? ")
        self.user_blog = None
        if self._user_exists():
            print("Welcome back {}".format(self.user))
        else:
            self._create_new_account()

    def _user_exists(self):
        blog = Database.find_one('blogs', {"author": self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    # may be made static. Why?
    def _create_new_account(self):
        title = input("Title of the blog? ")
        description = input("Description of the blog? ")
        blog = Blog(self.user, title, description)
        # no need to create new_post() because we are essentially creating a new account.
        blog.save_to_mongo()
        self.user_blog = blog

    def run_menu(self):
        read_or_write = input("Would you like to read (R) or write (W) a blog post? ")
        if read_or_write == "R":
            self._display_blogs()
            self._pick_blog()
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging...")

    def _display_blogs(self):
        blogs = Database.find('blogs', {})
        for blog in blogs:
            print("\n{}\n{}\n{}\n{}"
                  .format(blog['author'],
                          blog['title'],
                          blog['description'],
                          blog['id']))

    def _pick_blog(self):
        blog_choice = input("Enter blog id to read: ")
        self._show_posts(blog_choice)

    def _show_posts(self, choice):
        posts = Database.find('posts', {"blog_id": choice})
        for post in posts:
            print("\n{}\n{}\n{}\n"
                  .format(post['author'],
                          post['title'],
                          post['content']))

