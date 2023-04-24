const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

var fishRoutes = require('./routes/fish')
var priceRoutes = require('./routes/price')
var sliceRoutes = require('./routes/slice')
var qualityRoutes = require('./routes/quality')

var app = express()
app.use(bodyParser.json())
app.use(cors({origin:'http://localhost:3000'}))
app.listen(8000,()=>console.log('Server started at : 8000'))

app.use('/fish',fishRoutes)
app.use('/price',priceRoutes)
app.use('/slice',sliceRoutes)
app.use('/quality',qualityRoutes)
app.use(express.static('public'))