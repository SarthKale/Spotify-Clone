"""Creating a custom App Specific Middleware for common utilization"""
from .utils import SpotifyClone


class SpotifyMiddleware:
    """Creating a custom Spotify Middleware for common utilization"""
    def __init__(self, get_response):
        self.get_response = get_response
        self._spotify_clone = None

    def __call__(self, request):
        if not hasattr(request, 'spotify_clone'):
            setattr(request, 'spotify_clone', self.get_spotify_clone())
        return self.get_response(request)

    def get_spotify_clone(self):
        """Initializes the SpotifyClone class object for the Middleware"""
        if self._spotify_clone is None:
            self._spotify_clone = SpotifyClone()
        return self._spotify_clone
