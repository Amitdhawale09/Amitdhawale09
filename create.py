



def main():
    print(" Enter the file name that you want to create:");
    name=input();

    fd=open(name,"x");# x flag is used to create a new file if it is not present


    print("File gets created with the information as:",fd);

if __name__=="__main__":
    main();