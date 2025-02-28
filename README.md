# YouTube Audio Downloader with Metadata

This Python script allows you to download audio from YouTube videos and playlists, add metadata such as artist, album, and title, and optionally embed album art into each downloaded song. The script organizes the downloads into a folder named after the album and ensures that each track includes all necessary metadata and album art.

## Features

- Downloads audio from YouTube in MP3 format.
- Organizes downloads into an album-specific folder.
- Adds metadata including artist, album, and title.
- Embeds album art into each MP3 file.
- Supports both single video and playlist downloads.
- Logs important actions and errors to a `download_log.txt` file for troubleshooting and reference.

## Requirements

- Python 3.x
- `yt-dlp` (a powerful YouTube downloader)
- `eyed3` (for handling MP3 metadata)
- `Pillow` (for image processing)
- **ffmpeg** (required by `yt-dlp` for audio format conversion)
  
### Install Required Packages

You can install the required Python packages using `pip`:

```bash
pip install yt-dlp eyed3 pillow
```
You will need to install [ffmpeg](https://ffmpeg.org/download.html) and add it to your PATH

## Usage

To use the script, you can run it from the command line with the following syntax:

```bash
python download_audio.py <YouTube_URL> <Artist_Name> <Album_Name> <Album_Art_Path>
```

### Parameters:
- `<YouTube_URL>`: The URL of the YouTube video or playlist you want to download from.
- `<Artist_Name>`: The name of the artist.
- `<Album_Name>`: The name of the album.
- `<Album_Art_Path>`: The path to the image file you want to use as album art (optional).

### Example Usage:

```bash
python download_audio.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "Rick Astley" "Never Gonna Give You Up" "path_to_album_art.jpg"
```

### Notes:
- If you do not provide an album art image path, the script will skip adding album art.
- If the album folder already exists, it will not be recreated. The script will use the existing folder.

## Issues

This is still a work in proccess, I don't think the Album art is working correctly. That is why I have the log file still in the script.
The script logs important events and errors in a `download_log.txt` file located in the same directory as the script. The log will contain information such as folder creation, file renaming, metadata addition, and any errors that occur during the process.

## Acknowledgements

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for downloading YouTube videos and extracting audio.
- [eyed3](https://github.com/nicfit/eyed3) for adding and modifying MP3 metadata.
- [Pillow](https://pillow.readthedocs.io/en/stable/) for image handling and album art embedding.
- [ChatGPT](https://chatgpt.com/) for making the whole program.
