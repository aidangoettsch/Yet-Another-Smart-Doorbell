import face_recognition as fr
import os, glob

print(os.getcwd())
fileCount = len(os.listdir("pictures/base"))
print(fileCount)

baseImages = []
baseNames = []

os.chdir("pictures/base")
for f in glob.glob("*.png"):
    baseNames.append(f)
    print(f)

i = 0
while i < fileCount:
    baseImages.append(fr.load_image_file(baseNames[i]))


