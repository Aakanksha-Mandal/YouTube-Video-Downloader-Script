import os
from pytube import YouTube

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m' + '\033[4m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    ORANGE = '\033[38;2;255;165;0m'
    ENDC = '\033[0m'

def convert_seconds_to_hh_mm_ss(seconds):
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if hours == 0:
        return("{}:{}".format(minutes, seconds))
    else:
        return("{}:{}:{} seconds".format(hours, minutes, seconds))

try:
    url = input(colors.ORANGE + "Enter the YouTube URL: " + colors.ENDC)
    yt = YouTube(str(url))

    print(colors.MAGENTA + "\nTitle: " + colors.ENDC + yt.title)
    print(colors.MAGENTA + "Views:" + colors.ENDC, yt.views)
    print(colors.MAGENTA + "Channel: " + colors.ENDC + colors.BLUE + yt.channel_url + colors.ENDC)
    print(colors.MAGENTA + "Thumbnail: " + colors.ENDC + colors.BLUE + yt.thumbnail_url + colors.ENDC)
    print(colors.MAGENTA + "Length: " + colors.ENDC + convert_seconds_to_hh_mm_ss(yt.length))

    download_option = input(colors.YELLOW + "\nDownload Video(V) or Audio(A): " + colors.ENDC).upper()

    if download_option == 'V':
        available_streams = yt.streams.filter(progressive=True, file_extension='mp4')
        print(colors.YELLOW + "\nAvailable Resolutions:" + colors.ENDC)
        for i, stream in enumerate(available_streams):
            print(colors.YELLOW + "   " + f"{i+1}) {stream.resolution}" + colors.ENDC)
        selection = int(input(colors.YELLOW + "Enter the number corresponding to your desired resolution: " + colors.ENDC))
        selected_stream = available_streams[selection - 1]
    elif download_option == 'A':
        available_audio_streams = yt.streams.filter(only_audio=True)
        available_audio_streams = sorted(available_audio_streams, key=lambda x: int(x.abr.replace('kbps', '')))
        print(colors.YELLOW + "\nAvailable MP3 Options:" + colors.ENDC)
        for i, stream in enumerate(available_audio_streams):
            print(colors.YELLOW + "   " + f"{i+1}) Audio ({stream.abr})" + colors.ENDC)
        selection = int(input(colors.YELLOW + "Enter the number corresponding to your desired option: " + colors.ENDC))
        selected_stream = available_audio_streams[selection - 1]
    else:
        raise ValueError("Invalid option selected. Please choose 'V' for video or 'A' for audio.")

    download_dir = input(colors.ORANGE + "\nEnter the download directory: " + colors.ENDC)
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    print(colors.CYAN + "\nDownloading..." + colors.ENDC)
    selected_stream.download(download_dir)
    print(colors.GREEN + "Download Complete" + colors.ENDC)

except Exception as e:
    print(colors.RED + "An error occurred:" + str(e) + colors.ENDC)
