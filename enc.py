#!/usr/bin/python
import os , chardet
import subprocess

def file_size_mb(filePath):
    return float(os.path.getsize(filePath)) / (1024 * 1024)

current_dr = os.getcwd()
os.remove(os.path.join(current_dr,'icnv.sh'))

f = open('icnv.sh','w')

rootDir ='/mount/MOVIES/Movies'
for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        if (file.endswith(".srt") or file.endswith(".sub")):
            fil = (os.path.join(subdir, file))

            print " %s\n" %fil
            if file_size_mb(fil) <3:
                rawdata = open(fil, "r").read()

                result = chardet.detect(rawdata)
                res = result['encoding']
                if res == None:
                    res="None"
            else:
                res="UTF"

            if  not res.upper().__contains__("UTF"):
                print result['encoding']
                if res !='None':
                    from_lang = res
                else:
                    from_lang = 'windows-1256'
                a= "iconv -f %s -t utf-8 \"%s\" > \"%s.conv\"\n" %(from_lang,fil,fil)
                f.write(a)
                a= "mv \"%s.conv\" \"%s\"\n" %(fil,fil)
                f.write(a)


f.close()

subprocess.call(["chmod","777" , "icnv.sh"])
subprocess.call(["ss",rootDir])

subprocess.call(["ksh","icnv.sh"])
