# from importlib.resources import path
import os
import shutil
from tkinter import *
from tkinter import filedialog

# improving windows file Separator. Sorting them into theri respected folders
# Enchancement of windows filter function. Sorting files  on the basices of file extension
screen = Tk()
screen.title("file extractor")
canvas = Canvas(screen, width=600, height=400, background='#d8e3f2')
screen.wm_iconbitmap(os.getcwd() + r'\file_ico.ico')
# screen.wm_attributes('-transparentcolor','#224072')
canvas.pack()

dict_extensions = {
    'Audio_extensions': ('.mp3', '.m4a', '.wav', '.flac', '.aif', '.cda', '.mid', '.mpa', '.ogg', '.wma', '.wpl'),
    'Compressed_extensions': ('.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip'),
    'Disc_media_extensions': ('.bin', '.dmg', '.iso', '.toast', '.vcd'),
    'Data_database_extensions': ('.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml'),
    'Font_extensions': ('.fnt', '.fon', '.otf', '.ttf', '.odt', '.rtf', '.tex', '.txt', '.wpd'),
    'Documents_extensions': (".doc ", '.pdf', ".txt", '.docx'),
    'Image_extensions': ('.jpg', '.png', '.JPG', '.JPEG', '.PNG', '.jpeg', '.ai', '.bmp', '.gif', '.ico', '.ps', '.psd', '.svg', '.tif', '.tiff',),
    'Presentation_extensions': ('.key ', '.odp', '.pps ', '.ppt', '.pptx'),
    'Videos_extensions': ('.mp4', '.MKV', '.flV', '.mpeg', '.mkv', '.3g2', '.3gp', '.avi', '.h264', '.m4v', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob', '.wmv'),
    'Spreadsheet_extensions': ('.ods', '.xls', '.xlsm', '.xlsx'),
}


# Function
def Focus_In(e):
    
    if path_field.get() == "Path folder":
        path_field.delete(0, 'end')


def Focus_Out(e):

    if path_field.get() != None:
        path_field.insert(0, "Path folder")


def select_path():

    global path
    path = filedialog.askdirectory()
    path_field.delete(0, 'end')
    path_field.insert(0, path)

    select_btn.config(state=ACTIVE, command=file_sorter)


def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    print(files)
    return files


def file_sorter():
    
    path_list.delete(0, END)
    folderpath = path_field.get()
    # print(folderpath)
    for extension_type, extension_value in dict_extensions.items():
        folder_name = extension_type.split('_')[0] + ' Files'
        folder_path = os.path.join(folderpath, folder_name)

        # print(os.path.exists(folder_path))
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)

        # print(file_finder(folderpath,extension_value))
        if file_finder(folderpath, extension_value) == [] and len(os.listdir(folder_path)) == 0:
            os.rmdir(folder_path)
        else:
            for item in file_finder(folderpath, extension_value):
                path_list.insert(END, item)
                item_path = os.path.join(folderpath, item)
                item_new_path = os.path.join(folder_path, item)
                shutil.move(item_path, item_new_path)


#Label and Entry
logo_img = PhotoImage(file='file_logo.png')
canvas.create_image(300, 80, image=logo_img)
path_label = Label(screen, text='Select the folder location below: ', font=(
    'Bree Serif', 11, 'bold'), fg='white', background="#efb04f")  # ,bg='#787676',#224072
path_field = Entry(screen, width=50, font=('Calibri', 13))
path_field.insert(0, "Path folder")
path_field.pack(pady=90)


locate_btn = Button(screen, text="Search", width=5,
                    height=1, command=select_path)
select_btn = Button(screen, width=12, text='Arrange',
                    height=1, state=DISABLED, command=file_sorter)

#List Box
path_list = Listbox(screen, width=82, height=13, font=("Calibri", 11))
path_list.pack(padx=10, pady=10)

# Binding
path_field.bind('<FocusIn>', Focus_In)
path_field.bind('<FocusOut>', Focus_Out)

# Add to window
canvas.create_window(255, 100, window=path_field)
canvas.create_window(295, 70, window=path_label)
canvas.create_window(467, 101, window=locate_btn)
canvas.create_window(540, 100, window=select_btn)
canvas.create_window(300, 260, window=path_list)


screen.mainloop()