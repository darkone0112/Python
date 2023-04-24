try:
    text = "This is a test file \n This is a second line \n This is a third line"
    
    with open('C:\\Users\\menendezj\\Desktop\\Repos\\Python\\learning_py\\Assets\\test.txt', 'a') as file:# w = write, r = read, a = append
        file.write(text)
    print("File created.")
except FileNotFoundError:
    print("File not found")
finally:
    print("Finished.")