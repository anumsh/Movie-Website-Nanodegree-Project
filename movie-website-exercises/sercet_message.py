import os
def change_files():
    file_list=os.listdir("/home/anum/Documents/Udacity/stage-3/prank/prank")
    #print file_list
    save=os.getcwd()
    print save
    os.chdir("/home/anum/Documents/Udacity/stage-3/prank/prank")
    for file_name in file_list:
        print("old file_name  " +file_name)
        print("new_file_name  " + file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
        os.getcwd()         
change_files()
