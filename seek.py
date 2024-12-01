
def main():
    print(" Enter the file name that you want to create:");
    name=input();

    fd=open(name,"rb");

    print("Current offset is :",fd.tell()) ## tell(where are you in file.)
    
    data=fd.read(5);

    print("Data is:",data);

    print("Current offset is:",fd.tell());
    fd.seek(-5,2); ## skip the 'hi_' from world 
    print("Current offset is:",fd.tell());
    data=fd.read();
    print(data);


    print(data)
if __name__=="__main__":
    main();


