"""Creating views for the music_app"""
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(View):
    """Home View for music_app"""

    def _get_top_artists_data(self, _spotify_clone):
        return _spotify_clone.top_artists_data()

    def _get_top_tracks_data(self, _spotify_clone):
        return _spotify_clone.top_tracks_data()

    def get(self, request):
        """Logic to handle the get requests in the index view"""
        _spotify_clone = request.spotify_clone
        artists_data = self._get_top_artists_data(_spotify_clone)
        tracks_data = self._get_top_tracks_data(_spotify_clone)
        if (artists_data == [{}]) or (tracks_data == [{}]):
            return render(request=request, template_name='test_index.html')

        first_six_tracks_data = tracks_data[:6]
        second_six_tracks_data = tracks_data[6:12]
        third_six_tracks_data = tracks_data[12:18]

        context = {
            'artists_data': artists_data, 'first_six_tracks_data': first_six_tracks_data,
            'second_six_tracks_data': second_six_tracks_data,
            'third_six_tracks_data': third_six_tracks_data
        }
        return render(request,template_name='index.html', context=context)


class Music(View):
    """Music View for music_app"""

    def _get_track_metadata(self, _spotify_clone, song_id):
        return _spotify_clone.track_metadata(song_id)

    def get(self, request, song_id):
        """Logic to handle the get requests in the music view"""
        _spotify_clone = request.spotify_clone
        track_metadata = self._get_track_metadata(_spotify_clone, song_id)
        if isinstance(track_metadata, str):
            return redirect('/')
        return render(request, template_name='music.html', context=track_metadata)


class Profile(View):
    """Profile View for music_app"""

    def _get_artist_profile_data(self, _spotify_clone, artist_id):
        return _spotify_clone.get_artist_data(artist_id)

    def get(self, request, artist_id):
        """Logic to handle the get requests in the profile view"""
        _spotify_clone = request.spotify_clone
        artist_profile_data = self._get_artist_profile_data(_spotify_clone, artist_id)
        if isinstance(artist_profile_data, str):
            return redirect('/')
        return render(request=request, template_name='profile.html', context=artist_profile_data)


class Search(View):
    """Search view for music_app"""

    def _get_search_data(self, _spotify_clone, search_query):
        return _spotify_clone.get_search_data(search_query)

    def post(self, request):
        """Logic to handle the search post requests in the Search view"""
        _spotify_clone = request.spotify_clone
        search_query = request.POST.get('search_query')
        search_result = self._get_search_data(_spotify_clone, search_query)
        if isinstance(search_result,str):
            return redirect('/')
        return render(request, 'search.html', search_result)


class Signup(View):
    """Signup View for music_app"""

    def get(self, request):
        """Logic to handle the get requests in the signup view"""
        return render(request,template_name='signup.html')

    def post(self, request):
        """Logic to handle the post requests in the signup view"""
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if (User.objects.filter(email=email).exists()) or (User.objects.filter(
                username=username).exists()):
                messages.info(request=request, message="The User already exists")
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # Authenticating the user
                user = auth.authenticate(username=username,password=password)
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request=request, message="Password did not match")
            return redirect('signup')


class Login(View):
    """Login View for music_app"""

    def get(self, request):
        """Logic to handle the get requests in the login view"""
        return render(request,template_name='login.html')

    def post(self, request):
        """Logic to handle the post requests in the login view"""
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user is None:
            messages.info(request=request, message="User not found")
            return redirect('login')
        auth.login(request, user)
        return redirect('/')


class Logout(LoginRequiredMixin, View):
    """Logout View for music_app"""

    def get(self, request):
        """Logic to handle the get requests in the logout view"""
        auth.logout(request=request)
        return redirect('/')
