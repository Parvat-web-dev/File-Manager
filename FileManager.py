import os

class File_manager:
    def __init__(this, file_name_or_dir_name):
            this.file_name = (file_name_or_dir_name)

    #A function to create a new file!
    def create_new_file(this):
        #file_name = this.file_name
        file_name = this.file_name
        try:
            created_file = open(file_name, 'x')
            created_file.close()
            print('The file was created and closed!')
        except FileExistsError:
            print('The File already exsists!')
            print('Please try any other name')
        except :
            print('Some unknown error occured!')
            print('Try using some other file name!')

    #A file to delete an exsisting file.
    def delete_file(this, are_you_sure = False):
        try:
            if are_you_sure == True:
                print('Note : This operation will delete the file PERMENANTLY!')
                os.remove(this.file_name)
                print('File named \'',this.file_name,'\' was deleted!')
            if are_you_sure != True:
                print('The file was NOT DELETED!')
                print('If you want to delete it,')
                print('make the "are_you_sure" parameter "True".')
        except NotImplementedError:
            print('For some reason, the file was not deleted!')
            print('Please check the file\'s name, and')
            print('check whether the file exists in the given path!')

    #A function to create a new folder!
    def create_new_folder(this):
        try:
            a = os.mkdir(this.file_name)
            print('The folder named \'',this.file_name,'\' was CREATED!')
        except NotImplementedError:
            print('For some reason, the folder was not created!')

    #A function to delete an existing folder!
    def delete_folder(this):
        try:
            a = os.removedirs(this.file_name)
            print('The folder named \'',this.file_name,'\' was DELETED!')
        except NotImplementedError:
            print('For some reason, the folder was not created!')

    #A function to rename an existion folder!
    def rename_folder(this, new_name):
        try:
            old_name = this.file_name
            new_name = new_name
            os.rename(old_name, new_name)
        except FileNotFoundError:
            print('The file with the specified name was not found!')
        except:
            print('Some Error occured!')

    #A class to work with editing, creating, or deleting files!
    class File:

        #Getting the file name
        def __init__(this, file_name):
            this.file_name = (file_name)
            if not('.' in file_name):
                this.file_name = str(file_name)+'.txt'

        #A function to open an exsisting file!
        def open(this, mode = 'r'):
            try:
                file_name = open(this.file_name, mode)
                return file_name
            except FileNotFoundError:
                print('The file was not found!')
                print('Try checking the file name or,')
                print('the path of the file.')

        #A function to rename an exsisting file!
        def rename(this, new_name):
            try:
                old_name = this.file_name
                new_name = new_name
                os.rename(old_name, new_name)
            except FileNotFoundError:
                print('The file with the specified name was not found!')
            except:
                print('Some Error occured!')

        #A function to add text at the end of the given file!
        def append_text(this, text, close_file = True):
            try :
                file_name = open(this.file_name, 'a')
                text = str(text)
                file_name.write(text)
                if close_file == True:
                    file_name.close()
            except FileNotFoundError:
                print('The file Was not Found!')

        #A function to clear the given file and write the given text!
        def overwrite_text(this, text):
            try :
                print('Warning! This will overwrite the existing file!')
                file_name = open(this.file_name, 'w')
                text = str(text)
                file_name.write(text)
                if close_file == True:
                    file_name.close()
            except FileNotFoundError:
                print('The file Was not Found!')


