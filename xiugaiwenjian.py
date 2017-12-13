import os

PATH="F:\学习\吴恩达机器学习视频"
DIR = "lua.mp4.bili2api.1";

for filename in os.listdir(PATH):
    i = 1;
    for inerfilename in os.listdir(PATH+"/"+filename):
        if os.path.isdir(PATH+"/"+filename+"/"+inerfilename):
            i=1;
            try:
                for ininerfilename in os.listdir(PATH+"/"+filename+"/"+inerfilename):
                    if os.path.isdir(PATH+"/"+filename+"/"+inerfilename+"/"+ininerfilename):
                        os.rename(PATH+"/"+filename+"/"+inerfilename+"/"+ininerfilename+"/"+"0.blv",
                                  PATH+"/"+filename+"/"+inerfilename+"/"+ininerfilename+"/"+str(i)+".mp4")
                    i+=1;
            except:
                continue
