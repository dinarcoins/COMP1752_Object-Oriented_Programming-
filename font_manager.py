import tkinter.font as tkfont


def configure():
    # family = "Segoe UI"
    family = "Helvetica"
    # Get the default font of the Tkinter interface
    default_font = tkfont.nametofont("TkDefaultFont")
    # Configure default font with size 15 and font family as "Helvetica"
    default_font.configure(size=15, family=family)
    # Get the default font for text in the Tkinter interface
    text_font = tkfont.nametofont("TkTextFont")
    # Configure font for text with size 12 and font family as "Helvetica"
    text_font.configure(size=12, family=family)
    # Get the default font for fixed text in the Tkinter interface
    fixed_font = tkfont.nametofont("TkFixedFont")
    # Configure font for fixed text with size 12 and font family as "Helvetica"
    fixed_font.configure(size=12, family=family)
