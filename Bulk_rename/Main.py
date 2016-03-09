__author__ = 'premaseem'

import os

list_of_files = os.listdir("/Users/asee2278/gitRepo/petProjects/python_mini_projects/Bulk_rename/prank")
print list_of_files
current_working_dir = os.getcwd()
os.chdir("/Users/asee2278/gitRepo/petProjects/python_mini_projects/Bulk_rename/prank")
for file in list_of_files :
    new_name = file.translate(None,"0123456789")
    try :
        os.renames(file,new_name)
    except :
        print "cannot rename this file :-( "
    print new_name