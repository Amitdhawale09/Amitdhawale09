import os
import shutil

print("-----")
# Define the directory to organize and a dictionary of extensions
directory = os.path.join(os.path.expanduser("~"),"Desktop")

print("******")

extensions = {
    ".jpg":"Images",
    ".png":"Images",
    ".gif":"Images",
    ".avi":"Videos",
    ".doc":"Documents",
    ".pdf":"PDF_folder"
}

# Iterate over all items in the directory
for filename in os.listdir(directory):
    file_path= os.path.join(directory,filename)

    # Check if the item is a file
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        # Check if the extension is in the predefined list
        if extension in extensions:
            folder_name= extensions[extension]# Get the corresponding folder name
            folder_path =os.path.join(directory,folder_name)# Define the folder path
            os.makedirs(folder_path,exist_ok= True)# Create the folder if it doesn't exist
            destination_path = os.path.join(folder_path,filename)# Define the destination path
            shutil.move(file_path,destination_path)# Move the file to the destination

            print(f"Moved {filename} to {folder_name} folder.")
        
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    
    else: 
        print(f"Skipped {filename}. It is a directory.") 

print("File organization completed.")