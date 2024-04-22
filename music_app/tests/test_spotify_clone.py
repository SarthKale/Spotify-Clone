"""This is the unittesting code for the SpotifyClone class"""

import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.append(os.getcwd())
from music_app.utils import SpotifyClone


class TestSpotifyClone(unittest.TestCase):
    """The class for unit testing all methods of the SpotifyClone class"""
    def setUp(self):
        self.spotify_clone = SpotifyClone()

    @patch('requests.get')
    def test_top_artists_data(self, mock_get):
        """Mock the requests.get method to simulate API response for top-artists-data request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'artists': [
                {'name': 'Artist 1', 'id': 'artist_id_1', 'visuals': {'avatar': [
                    {'url': 'artist_url_1'}]}}
            ]
        }
        mock_get.return_value = mock_response
        # Assertions
        top_artists = self.spotify_clone.top_artists_data()
        self.assertIsInstance(top_artists, list)
        self.assertEqual(len(top_artists), 1)
        self.assertIsInstance(top_artists[0], dict)
        self.assertIn('name', top_artists[0])
        self.assertIn('artist_id', top_artists[0])
        self.assertIn('artist_url', top_artists[0])

    @patch('requests.get')
    def test_top_tracks_data(self, mock_get):
        """Mock the requests.get method to simulate API response for top-tracks-data request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'tracks': [
                {'id': 'track_id_1', 'name': 'Track 1', 'album': {'cover': [
                    {'url': 'cover_url_1'}]}},
                {'id': 'track_id_2', 'name': 'Track 2', 'album': {'cover': [
                    {'url': 'cover_url_2'}]}}
            ]
        }
        mock_get.return_value = mock_response
        # Assertions
        top_tracks = self.spotify_clone.top_tracks_data()
        self.assertIsInstance(top_tracks, list)
        self.assertEqual(len(top_tracks), 2)
        for track in top_tracks:
            self.assertIsInstance(track, dict)
            self.assertIn('track_id', track)
            self.assertIn('track_name', track)
            self.assertIn('cover_url', track)
            self.assertIn('artist_id', track)
            self.assertIn('artist_name', track)

    @patch('requests.get')
    def test_get_audio_url(self, mock_get):
        """Mock the requests.get method to simulate API response for audio-url request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'youtubeVideo': {'audio': [{'url': 'audio_url'}]}
        }
        mock_get.return_value = mock_response
        # Assertions
        audio_url = self.spotify_clone.get_audio_url("some_song_id")
        self.assertIsInstance(audio_url, str)
        self.assertTrue(len(audio_url) > 0)

    @patch('requests.get')
    def test_track_metadata(self, mock_get):
        """Mock the requests.get method to simulate API response for track-metadata request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'name': 'Track 1', 'durationText': '3:30', 'playCount': 100,
            'album': {'cover': [{'url': 'cover_url'}]},
            'artists': [{'name': 'Artist 1'}]
        }
        mock_get.return_value = mock_response
        # Assertions
        track_metadata = self.spotify_clone.track_metadata("some_song_id")
        self.assertIsInstance(track_metadata, dict)
        self.assertIn('track_id', track_metadata)
        self.assertIn('track_name', track_metadata)
        self.assertIn('cover_url', track_metadata)
        self.assertIn('play_count', track_metadata)
        self.assertIn('artists_name', track_metadata)
        self.assertIn('duration_text', track_metadata)
        self.assertIn('audio_url', track_metadata)

    @patch('requests.get')
    def test_get_artist_data(self, mock_get):
        """Mock the requests.get method to simulate API response for artist-data request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'name': 'Artist 1', 'stats': {'monthlyListeners': 100},
            'visuals': {'header': [{'url': 'poster_url'}]},
            'discography': {'topTracks': [{'id': 'track_id_1', 'name': 'Track 1', 'album': {
                'cover': [{'url': 'cover_url_1'}]}}]}
        }
        mock_get.return_value = mock_response
        # Assertions
        artist_data = self.spotify_clone.get_artist_data("some_artist_id")
        self.assertIsInstance(artist_data, dict)
        self.assertIn('artist_id', artist_data)
        self.assertIn('artist_name', artist_data)
        self.assertIn('poster_url', artist_data)
        self.assertIn('monthly_listeners', artist_data)
        self.assertIn('top_tracks', artist_data)

    @patch('requests.get')
    def test_get_search_data(self, mock_get):
        """Mock the requests.get method to simulate API response for search-data request"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'tracks': {'items': [
                {'id': 'track_id_1', 'name': 'Track 1', 'album': {'cover': [
                    {'url': 'cover_url_1'}]}, 'artists': [{'name': 'Artist 1'}]},
                {'id': 'track_id_2', 'name': 'Track 2', 'album': {'cover': [
                    {'url': 'cover_url_2'}]}, 'artists': [{'name': 'Artist 2'}]}
            ]}
        }
        mock_get.return_value = mock_response
        # Assertions
        search_data = self.spotify_clone.get_search_data("some_search_query")
        self.assertIsInstance(search_data, dict)
        self.assertIn('search_query', search_data)
        self.assertIn('search_results_count', search_data)
        self.assertIn('track_list', search_data)
        self.assertIsInstance(search_data['track_list'], list)
        self.assertEqual(len(search_data['track_list']), 2)
        for track in search_data['track_list']:
            self.assertIsInstance(track, dict)
            self.assertIn('track_id', track)
            self.assertIn('track_name', track)
            self.assertIn('track_image', track)
            self.assertIn('duration_text', track)
            self.assertIn('artists_name', track)

if __name__ == '__main__':
    unittest.main()
