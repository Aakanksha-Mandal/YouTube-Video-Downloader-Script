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

    available_streams = yt.streams.filter(progressive=True)
    print(colors.YELLOW + "\nAvailable Resolutions:" + colors.ENDC)
    for i, stream in enumerate(available_streams):
        print(colors.YELLOW + "   " + f"{i+1}) {stream.resolution}" + colors.ENDC)

    selection = int(input(colors.YELLOW + "Enter the number corresponding to your desired resolution: " + colors.ENDC))
    selected_stream = available_streams[selection - 1]

    download_dir = input(colors.ORANGE + "\nEnter the download directory: " + colors.ENDC)
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    print(colors.CYAN + "\nDownloading..." + colors.ENDC)
    selected_stream.download(download_dir)
    print(colors.GREEN + "Download Complete" + colors.ENDC)

except Exception as e:
    print(colors.RED + "An error occurred:" + str(e) + colors.ENDC)
