class Playlist:
    def __init__(self, playlist):
        self.playlist = playlist[:]

    def __len__(self):
        return len(self.playlist)

    def __getitem__(self, i):
        return self.playlist[i]

pl = Playlist(["Song A", "Song B", "Song C"])
print(len(pl)) # 3
print(pl[1]) # Song B
