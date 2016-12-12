import urllib
import time

opener = urllib.URLopener()

link = "http://simpsons.wikia.com/wiki/List_of_Episodes"

filename = "episodes_link.txt"

opener.retrieve(link, filename)
time.sleep(1)