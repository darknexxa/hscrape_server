import os
pdfdirectory = 'pdfall'
verbose = False #set to true if want to see the log
try:
    os.makedirs(pdfdirectory)
except FileExistsError:
    # directory already exists 
    pass