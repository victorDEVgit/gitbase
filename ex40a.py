song_lyrics = ["She told me put my heart in a bag",
                "And nobody gets hurt",
                "Now am running from a love",
                "Am not fast",
                "So I'm Making it worse",
                "Now am digging up a grave from my past",
                "I'm a whole different person",
                "It was a gift and a curse",
                "But I cannot reverse it"]

class Song():

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_song(self):
        for lines in self.lyrics:
            print(lines)
    
song = Song(song_lyrics)
song.sing_song()