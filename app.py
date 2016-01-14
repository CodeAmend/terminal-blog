from database import Database
from menu import Menu
from models.blog import Blog

__author__ = 'jslvtr'

Database.initialize()

menu = Menu()
menu.run_menu()