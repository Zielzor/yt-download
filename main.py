import yt_dlp

def download_video(url):
    # Options for yt-dlp
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
    }

    # Download the video using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # First, list available formats
            ydl.params['listformats'] = True
            ydl.extract_info(url, download=False)
            
            # Reset listformats option
            ydl.params['listformats'] = False

            # Ask user to choose a format
            format_code = input("Enter the format code you want to download: ")
            
            if format_code:
                ydl_opts['format'] = format_code
            else:
                print("No format selected. Exiting.")
                return

            # Download the video
            ydl.params.update(ydl_opts)
            ydl.download([url])
            print("Video downloaded successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Prompt the user to input a video URL
    video_url = input("Please enter the YouTube Shorts or Facebook video URL: ")

    # Call the download function with the provided URL
    download_video(video_url)