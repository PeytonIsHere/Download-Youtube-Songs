import os
import subprocess
import eyed3
from PIL import Image
import argparse
import logging

# Set up logging
logging.basicConfig(filename='download_log.txt', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def download_audio(youtube_url, artist, album, album_art_path):
    # Step 1: Create a new folder for the album
    album_folder = album.replace(" ", "_")  # Replace spaces with underscores for the folder name
    if not os.path.exists(album_folder):
        os.makedirs(album_folder)
        logging.info(f"Created folder: {album_folder}")
    else:
        logging.info(f"Folder {album_folder} already exists.")

    # Step 2: Download the audio
    logging.info("Downloading audio...")
    print("Downloading audio...")
    command = [
        "yt-dlp",
        "--extract-audio",
        "--audio-format", "mp3",  # Ensure the download is in mp3 format
        "--output", f"{album_folder}/%(title)s.%(ext)s",  # Specify the output directory and filename format
        youtube_url,
    ]
    subprocess.run(command)

    # Step 3: Process each downloaded MP3 file in the album folder
    mp3_files = [f for f in os.listdir(album_folder) if f.endswith(".mp3")]
    if not mp3_files:
        logging.error("No MP3 files found!")
        print("No MP3 files found!")
        return
    
    # Step 4: Add metadata and album art to each song
    for mp3_file in mp3_files:
        logging.info(f"Processing {mp3_file}...")
        print(f"Processing {mp3_file}...")

        # Clean the title by removing YouTube-specific parts
        cleaned_title = mp3_file.replace(" - YouTube", "").strip()
        os.rename(f"{album_folder}/{mp3_file}", f"{album_folder}/{cleaned_title}")
        logging.info(f"Renamed to: {cleaned_title}")
        print(f"Renamed to: {cleaned_title}")

        # Add metadata
        logging.info("Adding metadata...")
        print("Adding metadata...")
        audio_file = eyed3.load(f"{album_folder}/{cleaned_title}")
        if not audio_file.tag:
            audio_file.initTag()

        audio_file.tag.artist = artist
        audio_file.tag.album = album
        audio_file.tag.title = os.path.splitext(cleaned_title)[0]

        # Add album art to each song
        if album_art_path:
            logging.info("Adding album art...")
            print("Adding album art...")
            try:
                with open(album_art_path, "rb") as img_file:
                    audio_file.tag.images.set(3, img_file.read(), "image/jpeg", u"Album cover")
                logging.info("Album art added successfully.")
            except FileNotFoundError:
                logging.error(f"Album art not found at {album_art_path}. Skipping album art.")

        audio_file.tag.save()
        logging.info(f"Metadata added successfully to {cleaned_title}!")
        print(f"Metadata added successfully to {cleaned_title}!")

# Command-line argument parsing
parser = argparse.ArgumentParser(description="Download audio from YouTube and add metadata and album art.")
parser.add_argument("youtube_url", help="The URL of the YouTube video or playlist")
parser.add_argument("artist", help="The artist name")
parser.add_argument("album", help="The album name")
parser.add_argument("album_art", help="The path to the album art image file", nargs='?', default=None)

args = parser.parse_args()

download_audio(args.youtube_url, args.artist, args.album, args.album_art)
