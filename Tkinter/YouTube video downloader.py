from pytube import YouTube
print('===================')
# =========================
rerun = "y"
while rerun == "y":
    try:
        url = input('Enter the YouTube link for the video u want: \n')
        the_video = YouTube(url)
        # =========================
        print('===================')
        print('your video title: ', the_video.title)
        # =========================
        print('===================')
        the_video = the_video.streams.get_highest_resolution()
        print('Please wait until it finsh downloding ......')
        # =========================
        the_video.download()
        print('Done\' -_- \' (the video is installed in the folder you are in)')
        print('===================')
    except:
        print('Sorrry somethng went wrong')
        print('===================')
    rerun = input("Enter y to rerun or any thing else to end: ")
    print('===================')
