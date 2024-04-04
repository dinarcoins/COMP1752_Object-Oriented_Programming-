# create_video_list.py - Prototype GUI

import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content):  # inserts content into the text_area
    text_area.delete("1.0", tk.END)  # first the existing content is deleted
    text_area.insert(1.0, content)  # then the new content is inserted

class CreateVideoListApp:
    def __init__(self, window):
        self.window = window
        window.geometry('750x350')
        window.title("Create Video List")

        self.label = tk.Label(window, text="Enter video details:")
        self.label.pack()

        self.video_title_label = tk.Label(window, text="Title:")
        self.video_title_label.pack()
        self.video_title_entry = tk.Entry(window)
        self.video_title_entry.pack()

        self.video_url_label = tk.Label(window, text="URL:")
        self.video_url_label.pack()
        self.video_url_entry = tk.Entry(window)
        self.video_url_entry.pack()

        self.add_button = tk.Button(window, text="Add Video")
        self.add_button.pack()

        self.save_button = tk.Button(window, text="Save List")
        self.save_button.pack()


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    app = CreateVideoListApp(window)
    window.mainloop()
