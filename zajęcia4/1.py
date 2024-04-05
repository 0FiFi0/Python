import os
import shutil
shutil.rmtree("kopie")
os.mkdir("kopie")
raport = open("raport.txt", "w")

dir_names = ["wakacje", "wyjazd", "zima"]
for name in dir_names:
    files = os.listdir(name)
    raport.write(os.path.abspath(name)+ "\n")
    for index, file in enumerate(files):
        if file.lower().endswith(".jpg") or file.lower().endswith(".png") or file.lower().endswith(".jpeg"):
            raport.write(file + "\n")
            filename = name.upper()
            nr = index
            ext = file.split(".")[-1]
            shutil.copy(name+"/"+file,"kopie" + f"/{filename}_{nr}.{ext}")
raport.close()




