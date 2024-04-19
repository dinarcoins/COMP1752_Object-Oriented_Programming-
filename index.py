from tkinter import *
from font_manager import *
from check_videos import *
from create_video_list import *
from update_video import *

def main():
    window = Tk()
    window.geometry("520x150")
    window.title("Video Player")

    def createCheckVideosWindow(mainWindow):
        # Open the window to check videos
        checkVideoWindow(mainWindow)

    def createVideoCreationWindow(mainWindow):
        # Open the window to create a video list
        videoCreationWindow(mainWindow)

    def createVideoUpdateWindow(mainWindow):
        # Open the window to update videos
        updateVideoWindow(mainWindow)

    frame = Frame(window)
    frame.pack(expand=True, pady=0)

    # Create three buttons
    checkVideosButton = Button(frame, text="Check Videos",  command=lambda: createCheckVideosWindow(window))
    createVideoButton = Button(frame, text="Create Video List", command=lambda: createVideoCreationWindow(window))
    updateVideosButton = Button(frame, text="Update Videos", command=lambda: createVideoUpdateWindow(window))

    checkVideosButton.pack(side="left", padx=20)
    createVideoButton.pack(side="left", padx=20)
    updateVideosButton.pack(side="left", padx=20)

    # Start the main event loop
    window.mainloop()

if __name__ == '__main__':
    main()