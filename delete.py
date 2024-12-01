import os



def main():
    print(" Enter the file name that you want to create:");
    name=input();

    

    if os.path.exists(name):
        
        os.remove(name);
        print("Successfully deleted.",name);
    else:
        print("There is no such file.");

if __name__=="__main__":
    main();