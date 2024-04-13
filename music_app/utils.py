"""Creating a utility class for Spotify API requests"""
import requests


class SpotifyClone:
    """Creating a class to implement methods that operates on the Spotify API
    for the project utilities"""

    def __init__(self) -> None:
        """Initialize the common variables"""
        self.api_key = '839c8392b0msh80dc845e82cd612p17231cjsnfc23787354be'
        self.api_host = 'spotify-scraper.p.rapidapi.com'
        self.api_url = 'https://spotify-scraper.p.rapidapi.com/v1/'
        self.headers = {
            'X-RapidAPI-Key': self.api_key,
            'X-RapidAPI-Host': self.api_host
        }

    def top_artists_data(self):
        """Fetching data of top artists using Spotify API"""
        end_point = 'chart/artists/top'
        url = self.api_url+end_point
        response = requests.get(url=url, headers=self.headers, timeout=20)
        response_data = response.json()

        artists_info = []
        # name, id, artist_url
        if 'artists' in response_data:
            for artist in response_data['artists']:
                name = artist.get('name', 'No Name')
                artist_id = artist.get('id', 'No ID')
                artist_url = artist.get('visuals',{}).get('avatar', [{}])[0].get('url', 'No URL')
                artists_info.append({
                    'name': name, 'artist_id': artist_id, 'artist_url': artist_url
                })
        return artists_info

    def top_tracks_data(self):
        """Fetching data of top songs using Spotify API"""
        end_point = 'chart/tracks/top'
        url = self.api_url + end_point
        response = requests.get(url=url, headers=self.headers, timeout=20)
        response_data = response.json()

        track_details = []
        # track_id, track_name, artist_id, artist_name, cover_url
        if 'tracks' in response_data:
            for track in response_data['tracks']:
                track_id = track.get('id', 'No ID')
                track_name = track.get('name', 'No Name')
                artist_id = track.get('artists', [{}])[0].get('id', 'No Artist')
                artist_name = track.get('artists', [{}])[0].get('name', 'No Artist')
                cover_url = track.get('album', {}).get('cover', [{}])[0].get('url', 'No URL')
                track_details.append({
                    'track_id': track_id, 'track_name': track_name, 'cover_url': cover_url,
                    'artist_id': artist_id, 'artist_name': artist_name
                })
        return track_details

    def get_audio_url(self, song_id):
        """Fetching Audio URL of a song using Spotify API, song_id and song_name"""
        query_string = {'track': song_id}
        end_point = 'track/download'
        url = self.api_url + end_point
        response = requests.get(url=url, headers=self.headers, timeout=20, params=query_string)
        response_data = response.json()

        audio_url = response_data.get('youtubeVideo',{}).get('audio', [{}])[0].get('url', 'No URL')
        return audio_url

    def track_metadata(self, song_id):
        """Fetching metadata of a song using Spotify API and song_id"""
        end_point = 'track/metadata'
        url = self.api_url + end_point
        query_string = {'trackId': song_id}
        response = requests.get(url=url, headers=self.headers, timeout=20, params=query_string)
        response_data = response.json()

        # track_id, track_name, duration_text, cover_url, artists_name
        track_name = response_data.get('name')
        duration_text = response_data.get('durationText')
        play_count = response_data.get('playCount')
        cover_url = response_data.get('album', {}).get('cover', [{}])[0].get('url', 'No URL')
        artists = response_data.get('artists', [{}])
        artists_name = ", ".join([artist.get('name', 'No Artist') for artist in artists])

        audio_url = self.get_audio_url(song_id)

        track_metadata = {
            'track_id': song_id, 'track_name': track_name, 'cover_url': cover_url,
            'play_count': play_count, 'artists_name': artists_name, 'duration_text': duration_text,
            'audio_url': audio_url
        }
        return track_metadata

    def get_artist_data(self, artist_id):
        """Fetching data of an artist using Spotify API and artist_id"""
        end_point = 'artist/overview'
        url = self.api_url + end_point
        query_string = {'artistId': artist_id}
        response = requests.get(url=url, headers=self.headers, timeout=20, params=query_string)
        response_data = response.json()

        # artist_id, artist_name, poster_url, montlyListeners,
        # top_tracks[ track_id, track_name, track_image, duration_text, play_count, artists ]
        artist_name = response_data.get('name')
        monthly_listeners = response_data.get('stats',{}).get('monthlyListeners',0)
        poster_url = response_data.get('visuals', {}).get('header', [{}])[0].get('url','No URL')
        top_tracks = []
        for track in response_data['discography']['topTracks']:
            track_id = track.get('id', 'No ID')
            track_name = track.get('name', 'No Name')
            track_image = track.get('album', {}).get('cover', [{}])[0].get('url', 'No URL')
            duration_text = track.get('durationText')
            play_count = track.get('playCount')
            artists = track.get('artists')
            artists_name = ", ".join([artist.get('name', 'No Artist') for artist in artists])
            top_tracks.append({
                'track_id': track_id, 'track_name': track_name, 'track_image': track_image,
                'duration_text': duration_text, 'play_count': play_count,
                'artists_name': artists_name
            })
        artist_data = {
            'artist_id': artist_id, 'artist_name': artist_name, 'poster_url': poster_url,
            'monthly_listeners': monthly_listeners, 'top_tracks': top_tracks
        }
        return artist_data

    def get_search_data(self, search_query):
        """Fetching songs as the results of a search query using Spotify API"""
        end_point = 'search'
        url = self.api_url + end_point
        query_string = {'term': search_query, 'type': 'track'}
        response = requests.get(url=url, headers=self.headers, timeout=20, params=query_string)
        response_data = response.json()

        search_results_count = len(response_data['tracks']['items'])
        track_list = []
        # 'track_id', 'track_name', 'track_image', 'duration_text', 'play_count', 'artists_name'
        for track in response_data['tracks']['items']:
            track_id = track.get('id', 'No ID')
            track_name = track.get('name', 'No Name')
            track_image = track.get('album', {}).get('cover', [{}])[0].get('url', 'No URL')
            duration_text = track.get('durationText')
            # play_count = track.get('playCount')
            artists = track.get('artists')
            artists_name = ", ".join([artist.get('name', 'No Artist') for artist in artists])
            track_list.append({
                'track_id': track_id, 'track_name': track_name, 'track_image': track_image,
                'duration_text': duration_text, 'artists_name': artists_name
            })
        search_data = {
            'search_query': search_query, 'search_results_count': search_results_count,
            'track_list': track_list
        }
        return search_data
