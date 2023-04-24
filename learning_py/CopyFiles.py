#copyfile() = copy the contents of the source to the destination and
#copy() = copy the file and metadata
#copy2() = copy the file, metadata, and the file's permission mode

import shutil # import shutil module to use shutil.copyfile() function to copy a file

shutil.copyfile("C:\\Users\\menendezj\\Desktop\\Repos\\Python\\\learning_py\\CopyFiles.py", "C:\\Users\\menendezj\\Desktop\\Repos\\Python\\\learning_py\\Assets\\CopyFilesCopy.py") #arguments = source, destination