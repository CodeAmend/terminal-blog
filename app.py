from database import Database
from models.blog import Blog

__author__ = 'jslvtr'

Database.initialize()

blog = Blog(author="Bruce Bros",
            title="Blog of choice",
            description="Just one great article after another")


#new_post() asks us for information for new post. Creates post object and saves it with blog_id
blog.new_post()
#saves blog information to mongo
blog.save_to_mongo()


#blog_data = Blog.from_mongo(blog.id)

print(blog.get_posts())

