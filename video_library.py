from library_item import LibraryItem

video_list = [
    {"id": 1, "name": "Tom and Jerry", "director": "Fred Quimby", "rating": 4, "play_count": 100},
    {"id": 2, "name": "Breakfast at Tiffany's", "director": "Blake Edwards", "rating": 3, "play_count": 200},
    {"id": 3, "name": "Casablanca", "director": "Michael Curtiz", "rating": 5, "play_count": 150},
    {"id": 4, "name": "The Sound of Music", "director": "Robert Wise", "rating": 5, "play_count": 150},
    {"id": 5, "name": "Gone with the Wind", "director": "Victor Fleming ", "rating": 5, "play_count": 150},
    {"id": 6, "name": "The Golden King", "director": "DinarCoins ", "rating": 5, "play_count": 150},
]

# Create an empty dictionary to store library items
library = {}
# Add library items to the dictionary using keys
library["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
library["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5)
library["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2)
library["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1)
library["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3)
library["06"] = LibraryItem("The Golden King", "DinarCoins", 3)

# Function to list all library items with their information
def list_all(haveRaf: bool):
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info(haveRaf)}\n"
    return output

# Function to get the name of a library item given its key
def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

# Function to get the director of a library item given its key
def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None

# Function to get the rating of a library item given its key
def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

# Function to set the rating of a library item given its key and a new rating
def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
    except KeyError:
        return

# Function to get the play count of a library item given its key
def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

# Function to increment the play count of a library item given its key
def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
    except KeyError:
        return
