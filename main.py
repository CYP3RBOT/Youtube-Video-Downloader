from pytube import YouTube
import os
  
def download(link, path, filetype):

    if filetype.lower() not in ["mp3", "mp4", "mov", "wav"]:
        return "Filetype must be: mp3, mp4, mov, or wav"

    youtube = YouTube(link)

    print()
    print("Title: ",youtube.title)
    print("Number of views: ",youtube.views)
    print("Length of video: ",youtube.length,"seconds")
    print("Description: ",youtube.description)
    print("Ratings: ",youtube.rating)
    print()

    if filetype in ["mp3", "wav"]:
        video = youtube.streams.filter(only_audio=True).first()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + "." + str(filetype)
        os.rename(out_file, new_file)
        return "Download complete!"
    if filetype in ["mp4", "mov"]:
        video = youtube.streams.filter(progressive=True).last()
        out_file = video.download(output_path=path)
        base, ext = os.path.splitext(out_file)
        new_file = base + "." + str(filetype)
        os.rename(out_file, new_file)
        return "Download complete!"


video_url = str(input("Enter the URL of the video you want to download\n>> "))

print("Enter the destination (leave blank for current directory)")
destination = str(input(">> ")) or '.'

filetype = input("Filetype (leave blank for mp4)\n>> ") or "mp4"


print(download(video_url, destination, filetype))



