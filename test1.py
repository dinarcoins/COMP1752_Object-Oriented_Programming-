class Video:
    def __init__(self, id, name, director, rating, play_count):
        self.id = id
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Director: {self.director}, Rating: {self.rating}, Play Count: {self.play_count}"


def main():
    # Khởi tạo danh sách video
    video_list = [
        Video(1, "Video 1", "Director A", 4, 100),
        Video(2, "Video 2", "Director B", 3, 200),
        Video(3, "Video 3", "Director C", 5, 150)
    ]

    # Hiển thị danh sách video ban đầu
    print("Danh sách video ban đầu:")
    for video in video_list:
        print(video)

    # Thêm video mới
    new_video = Video(4, "Video 4", "Director D", 2, 50)
    video_list.append(new_video)

    # Tăng rating cho tất cả video
    print("\nTăng rating cho tất cả video:")
    for video in video_list:
        video.rating += 1
        print(video)

    # Xóa video có id = 2
    video_list = [video for video in video_list if video.id != 2]

    # Hiển thị danh sách video sau khi xóa
    print("\nDanh sách video sau khi xóa:")
    for video in video_list:
        print(video)

    # Thêm số lần phát mới cho video có id = 1
    for video in video_list:
        if video.id == 1:
            video.play_count += 1

    # Hiển thị danh sách video cuối cùng
    print("\nDanh sách video cuối cùng:")
    for video in video_list:
        print(video)


if __name__ == "__main__":
    main()
