songs = []

def add_song():
    title = input("Tên bài hát: ")
    artist = input("Ca sĩ: ")
    duration = int(input("Thời lượng (giây): "))
    songs.append({
        "title": title,
        "artist": artist,
        "duration": duration
    })
    print(">>> Đã thêm bài hát thành công!")

def view_playlist():
    if not songs:
        print("Playlist trống.")
        return
    for i, s in enumerate(songs, start=1):
        print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")

def search_by_artist():
    name = input("Nhập tên ca sĩ: ").lower()
    matches = [s for s in songs if s['artist'].lower() == name]
    if not matches:
        print("Không tìm thấy bài hát.")
        return
    for i, s in enumerate(matches, start=1):
        print(f"{i}. {s['title']} - {s['artist']} ({s['duration']}s)")

def main():
    while True:
        print("\n=== MUSIC PLAYLIST ===")
        print("1. Thêm bài hát")
        print("2. Xem playlist")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            add_song()
        elif choice == "2":
            view_playlist()
        elif choice == "3":
            search_by_artist()
        elif choice == "4":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
