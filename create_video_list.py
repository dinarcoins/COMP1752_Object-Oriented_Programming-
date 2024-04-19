import tkinter as tk
import tkinter.scrolledtext as tkst
from constants import video_list 

def videoCreationWindow(mainWindow): 
    def play_all_videos():
        for video in video_list:
            video["rating"] += 1
        set_bottom_text(get_video_info())  

    def list_all_videos():
        set_bottom_text(get_video_info()) 

    def list_video():
        set_text(get_video_info())

    def get_video_info():
        video_info = ""
        for video in video_list:
            video_info += f"ID: {video['id']}, Name: {video['name']}, Director: {video['director']}, Rating: {'*' * video['rating']}, Play Count: {video['play_count']}\n"
        return video_info

    def delete_video():
        id_to_delete = int(delete_id_entry.get())
        video_list[:] = [
            video for video in video_list if video["id"] != id_to_delete]
        set_bottom_text(get_video_info())
        delete_id_entry.delete(0, tk.END)

    def add_video():
        new_video = {
            "id": int(id_entry.get()),
            "name": name_entry.get(),
            "director": director_entry.get(),
            "rating": int(rating_entry.get()),
            "play_count": 0
        }
        video_list.append(new_video)
        list_all_videos()
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        director_entry.delete(0, tk.END)
        rating_entry.delete(0, tk.END)

    def set_text(content):
        video_text_area.delete("1.0", tk.END)
        video_text_area.insert("1.0", content)

    def set_bottom_text(content):
        video_list_text.delete("1.0", tk.END)
        video_list_text.insert("1.0", content)

    window = tk.Tk()
    window.title("Create Video")
    video_text_area = tkst.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
    video_text_area.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    id_label = tk.Label(window, text="ID:")
    id_label.grid(row=1, column=0, padx=5, pady=5)
    id_entry = tk.Entry(window, width=5)
    id_entry.grid(row=2, column=0, padx=5, pady=5)
    name_label = tk.Label(window, text="Name:")
    name_label.grid(row=1, column=1, padx=5, pady=5)
    name_entry = tk.Entry(window, width=20)
    name_entry.grid(row=2, column=1, padx=5, pady=5)
    director_label = tk.Label(window, text="Director:")
    director_label.grid(row=1, column=2, padx=5, pady=5)
    director_entry = tk.Entry(window, width=20)
    director_entry.grid(row=2, column=2, padx=5, pady=5)
    rating_label = tk.Label(window, text="Rating:")
    rating_label.grid(row=1, column=3, padx=5, pady=5)
    rating_entry = tk.Entry(window, width=5)
    rating_entry.grid(row=2, column=3, padx=5, pady=5)
    add_btn = tk.Button(window, text="Add", command=add_video)
    add_btn.grid(row=2, column=4, padx=10, pady=10)
    list_all_btn = tk.Button(window, text="List All", command=list_all_videos)
    list_all_btn.grid(row=3, column=0, padx=10, pady=10)
    play_all_btn = tk.Button(window, text="Play All", command=play_all_videos)
    play_all_btn.grid(row=3, column=1, padx=10, pady=10)
    delete_id_label = tk.Label(window, text="Delete ID:")
    delete_id_label.grid(row=3, column=2, padx=5, pady=5)
    delete_id_entry = tk.Entry(window, width=5)
    delete_id_entry.grid(row=3, column=3, padx=5, pady=5)
    delete_btn = tk.Button(window, text="Delete", command=delete_video)
    delete_btn.grid(row=3, column=4, padx=10, pady=10)
    video_list_text = tkst.ScrolledText(window, width=50, height=10, wrap=tk.WORD)
    video_list_text.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
    video_list_text.delete("1.0", tk.END)
    list_video()

    window.mainloop()
