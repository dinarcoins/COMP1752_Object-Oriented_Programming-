class LibraryItem:
    # Initialize a LibraryItem object with name, director and rating properties
    def __init__(self, name, director, rating=0):
        self.name = name
        self.director = director
        self.rating = rating
        # Initialize the play_count attribute with an initial value of 0
        self.play_count = 0

    def info(self, haveRaf: bool):
        # Returns a string containing information about the LibraryItem object
        if haveRaf : 
            return f"{self.name} - {self.director} {self.stars()}"
        else :
            return f"{self.name} - {self.director} "

    def stars(self):
        # Create a string of * signs corresponding to the rating of the LibraryItem object
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
