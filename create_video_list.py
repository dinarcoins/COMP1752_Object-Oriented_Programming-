# create_video_list.py - Prototype GUI

import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class CreateVideoListApp:
    def __init__(self, window):
        self.window = window
        window.geometry('750x350')
        window.title("Create Video")

        list_videos_btn = tk.Button(
        window, text="Add Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)

        
        play_video_btn = tk.Button(
        window, text="Play", command=self.list_videos_clicked)
        play_video_btn.grid(row=0, column=1, padx=10, pady=10)

        check_video_btn = tk.Button(
            window, text="Delete Video", command=self.delete_video_func)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.list_txt = tkst.ScrolledText(
            window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3,
                           sticky="W", padx=10, pady=10)

        self.video_txt = tk.Text(window, width=48, height=12, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4,
                             sticky="W", padx=10, pady=10)

        self.list_videos_clicked()

    def delete_video_func(self):
        self.status_lbl.configure(text="Delete Video button was clicked!")
        key = self.input_txt.get()
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
        else:
            set_text(self.video_txt, f"Video {key} not found")

    def list_videos_clicked(self):
        self.status_lbl.configure(text="Add Videos button was clicked!")
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)

    def play_video(self):
        self.status_lbl.configure(text="List Videos button was clicked!")
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    app = CreateVideoListApp(window)
    window.mainloop()
