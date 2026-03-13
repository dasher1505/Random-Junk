#VERY IMPORTANT NOTE
#THIS OVERWRITES FILES IF THEY HAVE THE SAME NAME
#USE AT YOUR OWN RISK IG
#todo:
#   fix overwriting
#   add some kind of preview run option
#   could arguably further split up sort_files -> function to handle filemove itself


import os
import sys
import shutil

def main():
    parent_dir = get_directory()
    os.chdir(parent_dir)

    create_folders(parent_dir)
    sort_files(parent_dir)


def get_directory(): #Get directory to tidy up
    current_directory = input("Directory to sort (1 to exit): ")
    while not os.path.isdir(current_directory):
        if current_directory == '1':
            sys.exit()
        print("Sorry, that doesn't exist.")
        current_directory = input("Directory to sort (1 to exit): ")
    
    return current_directory

def create_folders(parent_dir):
    #update as needed
    folders_needed = ['Documents', 'Images', 'Archives',
                      'Videos', 'osu! content', 'Code',
                      'Executables', 'Other']


    for folder in folders_needed:  #Create folders for sorting
        path = os.path.join(parent_dir, folder)
        if not os.path.isdir(path):
            os.mkdir(path)

def sort_files(parent_dir):
        #update as needed
        filetypes = {
        'pdf': 'Documents',
        'doc': 'Documents',
        'docx': 'Documents',
        'txt': 'Documents',
        'png': 'Images',
        'jpg': 'Images',
        'jpeg': 'Images',
        'webp': 'Images',
        'gif': 'Images',
        'zip': 'Archives',
        'rar': 'Archives',
        'mp4': 'Videos',
        'avi': 'Videos',
        'flv': 'Videos',
        'wmv': 'Videos',
        'osu': 'osu! content',
        'osk': 'osu! content',
        'osr': 'osu! content',
        'py': 'Code',
        'exe': 'Executables'
    }
        
        file_list = os.listdir()

        for file_name in file_list:
            file_to_move_path = os.path.join(parent_dir, file_name) #Get path to file

            if os.path.isdir(file_to_move_path): #Skip folders
                continue
            else:
                if '.' in file_name: #Get file extension
                    file_extension = file_name.lower().rsplit('.', 1)[1]
                else:
                    file_extension = ''

                if file_extension in filetypes: #Find destination
                    folder_to_move_to = os.path.join(parent_dir, filetypes[file_extension])
                else:
                    folder_to_move_to = os.path.join(parent_dir, 'Other')

                shutil.move(file_to_move_path, folder_to_move_to) #Move
main()