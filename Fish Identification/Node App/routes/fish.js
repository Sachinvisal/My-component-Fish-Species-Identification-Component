const express = require('express')
var router = express.Router()
const axios = require('axios')

router.post('/',(req,res)=>{
    const url ='http://localhost:7777/fish_indentification'
    
    const data = JSON.stringify({ url:req.body.url});
    axios.post(url,data, {
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => {
        console.log(data.data)
        res.send(JSON.stringify({"data":data.data}))
    });
})

module.exports = router