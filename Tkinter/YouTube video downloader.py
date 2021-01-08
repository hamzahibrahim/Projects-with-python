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
        choices = the_video.streams.filter(progressive=True)
        print('please choose one:','\n==================')
        for i in choices:
            print(i)
        user_choice = int(input('Please enter your choice (by nubers(1,2,3,....)): '))
        the_choice = choices[user_choice-1]
        # =========================
        print('===================')
        print('Please wait until it finsh downloding ......')
        the_choice.download()
        # =========================
        print('Done\' -_- \' (the video is installed in the folder you are in)')
        print('===================')
    except:
        print('Sorrry somethng went wrong')
        print('===================')
    rerun = input("Enter y to rerun or any thing else to end: ")
    print('===================')
