import tkinter as tk


import font_manager as fonts
from check_videos import CheckVideos

# Function to handle the "Check Videos" button click event
def check_videos_clicked():
    # Update the status label text
    status_lbl.configure(text="Check Videos button was clicked!")
    # Open a new window for checking videos
    CheckVideos(tk.Toplevel(window))

# Create the main window
window = tk.Tk()
window.geometry("520x150")
window.title("Video Player")

fonts.configure()
# Create a label for the header
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Create the "Check Videos" button
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)
# Create the "Create Video List" button
create_video_list_btn = tk.Button(window, text="Create Video List")
create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)
# Create the "Update Videos" button
update_videos_btn = tk.Button(window, text="Update Videos")
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)
# Create a label for the status
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
# Run the main window's event loop
window.mainloop()
