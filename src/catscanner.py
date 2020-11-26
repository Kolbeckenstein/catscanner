import os

dataDir = os.getcwd() + "/data/CAT_00"
file_list = sorted(os.listdir(dataDir))

image_list = []
data_list = []

for file in file_list:
    if ".cat" in file:
        data_list.append(file)
    else:
        image_list.append(file)
