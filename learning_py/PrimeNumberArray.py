#make a for loop that will fill a array with 10 random numbers between 1 and 100,will print them and say wich one of them is prime

def main():
    import random
    arr = []
    for i in range(10):
        arr.append(random.randint(1,100))
    print(arr)
    for i in range(10):
        if arr[i] % 2 == 0:
            print(arr[i], "is not prime")
        else:
            print(arr[i], "is prime")
            
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()