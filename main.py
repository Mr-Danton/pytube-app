from pytube import YouTube

download_folder = "/home/jordan/Videos/Pytube"
url = "https://www.youtube.com/watch?v=C82lT9cWQiA"

video_object = YouTube( url )

stream = video_object.streams.get_highest_resolution()
stream.download( download_folder )