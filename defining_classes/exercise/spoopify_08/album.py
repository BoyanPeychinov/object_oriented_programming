from spoopify.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [s for s in songs]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."
        elif self.published:
            return "Cannot remove songs. Album is published."
        else:
            [self.songs.remove(s) for s in self.songs if song_name == s.name]
            return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = f"Album {self.name}\n"
        info += ''.join(f"== {s.name} - {s.length}\n" for s in self.songs)
        return info
