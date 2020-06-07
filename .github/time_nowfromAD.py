def time_nowfromAD():
    import time
    t = time.time()
    seconds = int(t % 60)
    minutes_whole = t // 60
    hours_whole = minutes_whole // 60
    minutes = int(minutes_whole % 60)
    days_whole = int(hours_whole // 24)
    hours = int(hours_whole % 24)

    print('Now from AD:')
    print(days_whole,'days,',hours,'hours,',minutes,'minutes,',seconds,'seconds.')

