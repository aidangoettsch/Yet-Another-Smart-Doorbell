import face_recognition as fr
import os, glob, socket, time
from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

#Setup
print(os.getcwd())
fileCount = len(os.listdir("pictures/base"))

imageArray = []
baseImages = []
baseFilenames = []
baseNames = []
resultsArray = []
encodedArray = []

os.chdir("pictures/base")
for f in glob.glob("*.png"):
    baseFilenames.append(f)

i = 0
while i < fileCount:
	baseImages.append(fr.load_image_file(baseFilenames[i]))
	i += 1

for img in baseImages:
    encodedArray.append(fr.face_encodings(img)[0])

#Webserver
hostName = ""
hostPort = 6969

class MyServer(BaseHTTPRequestHandler):
	def do_POST(self):
		global imageArray
		print( "Incoming HTTP: ", self.path )

		contentLength = int(self.headers['Contect Length'])
		postData = self.rfile.read(contentLength)
		img = base64.decodebytes(postData)
		imageArray = np.array(img, dtype='uint8')

		self.send_response()
		client.close()


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
print(baseNames)

unknownEncode = fr.face_encodings(fr.load_image_file(imageArray))

j = 0
while j < len(baseImages):
    result = fr.compare_faces([encodedArray[i]], unknownEncode)
    resultsArray.append(result)
    j += 1
