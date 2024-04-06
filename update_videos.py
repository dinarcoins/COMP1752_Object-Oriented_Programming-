# update_videos.py - Prototype GUI

import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content): # inserts content into the text_area      
    text_area.delete("1.0", tk.END) # first the existing content is deleted     
    text_area.insert(1.0, content) # then the new content is inserted 


class UpdateVideosApp:
    def __init__(self, master):
        self.master = master
        master.title("Update Videos")
        master.geometry('750x350')

        self.label = tk.Label(master, text="Select video to update:")
        self.label.pack()

        self.video_listbox = tk.Listbox(master)
        self.video_listbox.pack()

        self.edit_button = tk.Button(master, text="Edit Selected")
        self.edit_button.pack()

        self.delete_button = tk.Button(master, text="Delete Selected")
        self.delete_button.pack()

        self.update_button = tk.Button(master, text="Update List")
        self.update_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    fonts.configure()
    app = UpdateVideosApp(root)
    root.mainloop()
