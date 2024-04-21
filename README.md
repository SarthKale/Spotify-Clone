![Spotify-Clone Logo](https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_RGB_Green.png)

# Spotify-Clone

The Spotify-Clone aims to replicate the core functionalities and user interface of the popular music streaming service, Spotify. This application allows users to enjoy music, explore new tracks, and various other activities.

## Requirements

- docker
- docker-compose

## Getting Started
To clone this repository, run the following in a terminal.

```bash
# Clone the repository
git clone https://github.com/SarthKale/spotify-clone.git
# Navigate to the project directory:
cd spotify-clone
```

## Features

- **Music Streaming**: Stream your favorite songs instantly.
- **Search Functionality**: Easily search for songs.
- **User Authentication**: Users can sign up, log in, and log out securely.
- **Responsive Design**: The app is optimized for both desktop and mobile devices.

## Run Application
You can run this application in 2 ways - 1. Locally, 2. Inside Docker.

### Run Locally

Make sure you have python3.10 or higher installed on your system.
```bash
# Create a virtual environment
python -m venv env
# Activate the virtual environment
source env/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run migrations
python manage.py migrate
# Start the development server
python manage.py runserver
```

### Run Inside a Docker Container

```bash
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up
```

Open your browser, go to `localhost` to access the app.

## Usage

- Open your web browser and navigate to http://localhost to access the app.
- **Stream Music**: Click on a song to start streaming and hit the play button.
- **Explore**: Discover new music by searching for artists or tracks.
- **Sign Up**: Create a new account by providing your email address and password.
- **Log In**: Log in to your account with the credentials.

## Technologies Used

- **Python**
- **Django**
- **HTML/CSS/JavaScript**
- **Bootstrap**

## Author

Sarthak Kale
