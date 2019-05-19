import os
pdfdirectory = 'static/pdfall'
imagedirectory = 'static/scrapped'
hlist = ['nhentai','erolord']
verbose = False #set to true if want to see the log
try:
    os.makedirs(pdfdirectory)
    os.makedirs(imagedirectory)
except FileExistsError:
    # directory already exists 
    pass