import face_recognition as fr
import os, glob



baseImages = []
baseNames = []

os.chdir("/pictures/base")
for file in glob.glob("*.png"):
    baseNames.append(file)

i = 0
while i < fileCount:
    baseImages.append(fr.load_image_file(baseNames[i]))
