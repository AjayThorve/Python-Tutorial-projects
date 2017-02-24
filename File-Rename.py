import os
def file_rename():
    list=os.listdir("/Users/ajayanilthorve/Desktop/Udacity/python_tut/prank")
    print list
    os.chdir("/Users/ajayanilthorve/Desktop/Udacity/python_tut/prank")
    for file_name in list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    print list
file_rename()