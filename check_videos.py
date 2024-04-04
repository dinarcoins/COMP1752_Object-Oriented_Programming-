import tkinter as tk
import tkinter.scrolledtext as tkst


import video_library as lib
import font_manager as fonts


def set_text(text_area, content): # inserts content into the text_area      
    text_area.delete("1.0", tk.END) # first the existing content is deleted     
    text_area.insert(1.0, content) # then the new content is inserted 


class CheckVideos(): 
    def __init__(self, window):
        # Set the size of the window to 750x350 pixels
        window.geometry("750x350") 
        # Set the window's title to "Check Videos" 
        window.title("Check Videos")  

        # Create a Button with the content "List All Videos", which when clicked will call the self.list_videos_clicked() method.
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked) 
        # Place the Button in the window with position row 0, column 0 and spacing padx=10, pady=10.
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10) 

        # Create a Label with the content "Enter Video Number".
        enter_lbl = tk.Label(window, text="Enter Video Number") 
        # Place the Label in the window with position row 0, column 1 and spacing padx=10, pady=10.
        enter_lbl.grid(row=0, column=1, padx=10, pady=10) 

        # Create an Entry with a width of 3.
        self.input_txt = tk.Entry(window, width=3)
        # Place Entry into window with position row 0, column 2 and spacing padx=10, pady=10 
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) 


        # Create a Button with the content "Check Video", which when clicked will call the self.check_video_clicked() method.
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked) 
        # Place the Button in the window with position row 0, column 3 and spacing padx=10, pady=10.
        check_video_btn.grid(row=0, column=3, padx=10, pady=10) 

        # Create a ScrolledText with a width of 48 and a height of 12.
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none") 
        # Place the ScrolledText in the window with position row 1, colum 0, spans 3 column spaces, stick to the West (sticky="W") and spacing padx=10, pady=10.
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10) 

        # Create a Text with a width of 24 and a height of 4.
        self.video_txt = tk.Text(window, width=24, height=4, wrap="none")
        # Place the Text in the window with position row 1, column 3 and stick to the northwest (sticky="NW") and spacing padx=10, pady=10. 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10) 

        # Create a Label with empty content and font "Helvetica" with size 10.
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) 
        # Place the Label in the window with position row 2, column 0, spans 4 column spaces and stick to the west (sticky="W") and spacing padx=10, pady=10.
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10) 

        # Call self.list_videos_clicked() method.
        self.list_videos_clicked() 

    def check_video_clicked(self):
        # Get value from input_txt cell
        key = self.input_txt.get()
        # Get video name based on key from library (lib)
        name = lib.get_name(key)
        if name is not None:
            # Get the director of the video from the library (lib)
            director = lib.get_director(key)
            # Get the video's rating from the library (lib)
            rating = lib.get_rating(key)
            # Get the video's play count from the library (lib)
            play_count = lib.get_play_count(key)
            # Create a string video_details containing information about the video
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            # Display video_details on the video_txt cell
            set_text(self.video_txt, video_details)
        else:
            # If the video is not found, display the message not found
            set_text(self.video_txt, f"Video {key} not found")
        # Update status_lbl label to "Check Video button was clicked!"
        self.status_lbl.configure(text="Check Video button was clicked!")

    def list_videos_clicked(self):
        # Get list of all videos from library (lib)
        video_list = lib.list_all()
        # Display the video list in the list_txt cell
        set_text(self.list_txt, video_list)
        # Update status_lbl label to "List Videos button was clicked!"
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    CheckVideos(window)     # open the CheckVideo GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc
