const express = require('express')
const app = express()

const PORT = 3000

const bodyParser = require('body-parser')
const expressFileUpload = require('express-fileupload')

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