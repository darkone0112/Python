try:
    with open('C:\\Users\\menendezj\\Desktop\\Repos\\Python\\learning_py\\Assets\\test.txt') as file:
        print(file.read())   
except FileNotFoundError as e:
    print("File not found")
    print(e)
finally:
    print("Finished.")
    
