import face_recognition as fr
import numpy as np
import os, glob, socket, time
from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

#Setup
fileCount = len(os.listdir("pictures/base"))

imageArray = []
baseImages = []
baseFilenames = []
baseNames = []
resultsArray = []
encodedArray = []

for f in glob.glob("pictures/base/*.png"):
    baseFilenames.append(f)
#print(baseFilenames)
i = 0
while i < fileCount:
	baseImages.append(fr.load_image_file(baseFilenames[i]))
	i += 1

for img in baseImages:
    encodedArray.append(fr.face_encodings(img)[0])

#Webserver
hostName = ""
hostPort = 6969

cache_file = open("cache.txt", "wb")

class MyServer(BaseHTTPRequestHandler):
	def do_POST(self):
		global imageArray
		global cache_file
		print( "Incoming HTTP: ", self.path )

		contentLength = int(self.headers['Content-Length'])
		#print(contentLength)
		postData = self.rfile.read(contentLength)
		#print(postData)
		cache_file.write(postData)
		#img = base64.decodebytes(postData)
		#print(img)
		#imageArray = np.array(img, dtype='uint8')
		#cache_file.close()
		self.send_response(200)
		#client.close()


myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

#Comparison
for fname in baseFilenames:
	baseNames.append(fname[0:(len(fname)-4)])

unknownEncode = fr.face_encodings(fr.load_image_file(cache_file))
cache_file.close()
j = 0
while j < len(baseImages):
	result = fr.compare_faces([encodedArray[i]], unknownEncode)
	resultsArray.append(result)
	j += 1
if True in resultsArray:
	print("Face Matched!")
else:
	print("No match found.")
