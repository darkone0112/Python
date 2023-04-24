import os # import os module to use os.path.exists() function to check if a file exists or not 
path = "C:\\Users\\menendezj\\Desktop\\Repos\\Python\\learning_py\\scope.py" # path to the file we want to check if it exists or not
if os.path.exists(path): # if the file exists
    print("The file exists") # print the message
    if os.path.isfile(path):
        print("The path is a file")
    elif os.path.isdir(path):
        print("The path is a directory")
else: # if the file does not exist
    print("The file does not exist")