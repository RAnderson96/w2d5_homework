import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.playlist= Song()

        self.guest1 = Guest("Bob", 18, "Love Story - Taylor Swift", 50.00) 

    def test_can_add_song(self):
        self.guest1.add_song_to_list("Here to Stay - Korn", self.playlist)
        print(self.playlist.song_list)
        self.assertEqual("Here to Stay - Korn", self.playlist.song_list[0])

    def test_check_song_added(self):

        self.guest1.add_song_to_list("Here to Stay - Korn", self.playlist)
        result = self.guest1.check_song_in_playlist("Here to Stay - Korn", self.playlist)
        self.assertEqual(True, result)

    def test_check_song_not_added(self):
        result = self.guest1.check_song_in_playlist("Here to Stay - Korn", self.playlist)
        self.assertEqual(False, result)

    def test_fav_song(self):
        self.guest1.add_song_to_list("Love Story - Taylor Swift", self.playlist)
        output = self.guest1.guest_fav_song_in_playlist(self.playlist, self.guest1)
        
        self.assertEqual("Whoo!", output)

