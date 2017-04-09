def TimerVLC(nameFile, path, time):
    file = path + " \ ".strip() + nameFile + ".srt"
    with open(file, "w") as file:
        i = 0
        sec = 0

        strTime = "00:00:"

        while i < time*100:
            i += 1
            begtime = str('%.3f' % sec).replace(".", ",")
            endtime = str('%.3f' % (sec+0.01)).replace(".", ",")

            file.write(str(i) + "\n")
            file.write(strTime + begtime + " --> " + strTime + endtime + "\n")
            file.write(begtime + "\n")
            file.write("\n")
            sec += 0.01



#On creer une string toute les centièmes de secondes
#Max une minute --> Evolution

TimerVLC("test", r"C:\Users\Admin\Downloads", 10)
