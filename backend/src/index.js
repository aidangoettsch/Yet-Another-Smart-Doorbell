const express = require('express')
const http = require('http')
const app = express()

const smartThings = require('smartthings-node').SmartThings

let st = new smartThings("c218c3a4-6ba6-4463-ba6a-dbb35ec94b39")
st.devices.listDevicesByCapability('switch')
.then(deviceList => {
  console.log(deviceList);
})


const PORT = 3002

const bodyParser = require('body-parser')
const expressFileUpload = require('express-fileupload')

let wsHttpServer = http.createServer()
wsHttpServer.listen(8069)

const WebSocketServer = require('websocket').server
const wsConfig = {
  httpServer: wsHttpServer,
  maxReceivedFrameSize: 1024,
  maxReceivedMessageSize: 10000
}
console.log('INFO > Web Socket HTTP started on: ' + 8069)

const wsServer = new WebSocketServer(wsConfig);

wsServer.on('request', (request) => {
  const connection = request.accept(null, request.origin);

  connection.on('message', function(message) {
    console.log(message)
  })

  connection.on('close', function(connection) {
    // close user connection
  })
})






app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))
app.use(expressFileUpload())

app.post('/faceframe', (req, res) => {
  console.log(req.body)
  // if (!err && req.code === 200) {
  //
  // } else console.error(err)
})


app.listen(PORT)
console.log(`[INFO] Listening on port ${PORT}`)