import tkinter as tk
import tkinter.scrolledtext as tkst
from video_library import video_list 

def checkVideoWindow(mainWindow):
    def list_all_videos():
        video_info = get_video_info()
        set_bottom_text(video_info)

    def check_video():
        id_to_check = int(id_entry.get())
        video_info = get_video_info_by_id(id_to_check)
        set_text(video_info)

    def get_video_info():
        info = ""
        for video in video_list:
            info += f"ID: {video['id']}, Name: {video['name']}, Director: {video['director']}, Rating: {'*' * video['rating']}\n"
        return info

    def get_video_info_by_id(id):
        for video in video_list:
            if video['id'] == id:
                return f"ID: {video['id']}, Name: {video['name']}, Director: {video['director']}, Rating: {'*' * video['rating']}"
        return "Video not found."

    def set_text(content):
        video_text_area.delete("1.0", tk.END)
        video_text_area.insert("1.0", content)

    def set_bottom_text(content):
        video_list_text.delete("1.0", tk.END)
        video_list_text.insert("1.0", content)

    window = tk.Tk()
    window.title("Check Video")
    id_label = tk.Label(window, text="Enter Video ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(window, width=10)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    check_btn = tk.Button(window, text="Check Video", command=check_video)
    check_btn.grid(row=0, column=2, padx=5, pady=5)
    video_text_area = tkst.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
    video_text_area.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    list_all_btn = tk.Button(window, text="List All Videos", command=list_all_videos)
    list_all_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
    video_list_text = tkst.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
    video_list_text.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    window.mainloop()
