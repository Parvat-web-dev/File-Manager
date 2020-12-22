import FileManagerModule as fm
from tkinter import *

###    Creating a File Manager Application!    ###

#Some variables
bg_color = 'black'
text_color = 'white'


#The main window
window = Tk()
window.geometry('600x500')
window.config(bg = bg_color)

#The file name Entry
file_name_label = Label(window, text = 'File/Dir Name:', font = 'Courier 18', fg = 'white', bg = 'black')
file_name_label.place(x = 5, y = 100)

file_name_entry = Entry(window, font='Courier 20', fg = 'white', bg = 'blue')
file_name_entry.place(x = 210, y = 100)

#the file rename entry
rename_label = Label(window, text = '***Rename As:', font = 'Courier 18', fg = 'white', bg = 'black')
rename_label.place(x = 5, y = 150)

rename_entry = Entry(window, font='Courier 20', fg = 'white', bg = 'blue')
rename_entry.place(x = 210, y = 150)

#The options
opt1 = ['Create', 'Delete', 'Rename']
opt2 = ['A File', 'A Dir.']

main_options = StringVar()
main_options.set(opt1[0])


sub_options = StringVar()
sub_options.set(opt2[0])

opt_1 = OptionMenu(window, main_options, *opt1)
opt_1.config(font = 'Courier 20')
opt_1.place(x = 150,y = 200)
opt_2 = OptionMenu(window, sub_options, *opt2)
opt_2.config(font = 'Courier 20')
opt_2.place(x = 300,y = 200)

#The ok button.
def ok():
    file_name = file_name_entry.get()
    print(file_name)
    main = main_options.get()
    sub = sub_options.get()
    Rename = rename_entry.get()
    a = fm.File_manager(file_name)
    if main == opt1[0]:#Create
        
        if sub == opt2[0]:#New File
            a.create_new_file()
            print('Create a new file')
        if sub == opt2[1]:#New dir
            a.create_new_folder()
            print('New dir')
            
    if main == opt1[1]:#Delete
        if sub == opt2[0]:#A file
            a.delete_file(are_you_sure = True)
            print('Delete a file')

        if sub == opt2[1]:#A dir
            a.delete_folder()
            print('Delete a dir')

    if main == opt1[2]:#Rename
        if sub == opt2[0]:#file
            a.File(file_name).rename(Rename)
            print('Rename File')
        if sub == opt2[1]:#A dir
            a.rename_folder(Rename)
            print('Rename a dir')
    #At last:
    file_name_entry.delete(0, END)
    rename_entry.delete(0, END)


ok_btn = Button(window, text = '  Ok  ', fg = 'white', bg = 'green', font = 'Courier 18', command = ok)
ok_btn.place(x = 270, y = 400)

window.mainloop()
