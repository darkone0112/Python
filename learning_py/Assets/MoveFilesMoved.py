import os
import os

source = "C:\\Users\\menendezj\\Desktop\\Repos\\Python\\\learning_py\\MoveFiles.py"
destination = "C:\\Users\\menendezj\\Desktop\\Repos\\Python\\\learning_py\\Assets\\MoveFilesMoved.py"

try:
    if os.path.exists(destination):
        print("File already exists")
        print("Do yoy want to delete it?")
        if input() == "yes":
            os.remove(destination)
            print("File deleted")
            os.replace(source,destination)
        else:
            print("File not deleted")
    else:
        os.replace(source,destination)
except FileNotFoundError:
    print("File not found")
finally:
    print("Finished.")