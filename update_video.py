import tkinter as tk
from constants import video_list 

def updateVideoWindow(mainWindow):
    def update_video_rating():
        try:
            # Get ID and new rating from user input
            id_to_update = int(id_entry.get())
            new_rating = int(new_rating_entry.get())

            # Find the video with the given ID and update its rating
            updated_video = None
            for video in video_list:
                if video['id'] == id_to_update:
                    video['rating'] = new_rating
                    updated_video = video
                    break

            if updated_video:
                set_text(f"Rating of video with ID {id_to_update} updated to {new_rating}.\nUpdated Video Info:\n{updated_video}")
            else:
                set_text(f"Video with ID {id_to_update} not found.")
        except ValueError:
            set_text("Please enter valid ID and new rating.")

    def set_text(content):
        update_text_area.delete("1.0", tk.END)
        update_text_area.insert("1.0", content)
    window = tk.Tk()
    window.title("Update Video")
    id_label = tk.Label(window, text="Enter Video ID:")
    id_label.grid(row=0, column=0, padx=5, pady=5)
    id_entry = tk.Entry(window, width=10)
    id_entry.grid(row=0, column=1, padx=5, pady=5)
    new_rating_label = tk.Label(window, text="Enter New Rating:")
    new_rating_label.grid(row=1, column=0, padx=5, pady=5)
    new_rating_entry = tk.Entry(window, width=10)
    new_rating_entry.grid(row=1, column=1, padx=5, pady=5)
    update_btn = tk.Button(window, text="Update Video", command=update_video_rating)
    update_btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    update_text_area = tk.Text(window, width=50, height=10)
    update_text_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    window.mainloop() 

