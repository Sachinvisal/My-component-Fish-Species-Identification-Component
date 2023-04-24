const express = require('express')
var router = express.Router()
const axios = require('axios')

router.post('/',(req,res)=>{
    const url ='http://localhost:5555/fish_price'
    
    const data = JSON.stringify({ Fish_Type:req.body.Fish_Type,Days:req.body.Days,Province:req.body.Province});
    axios.post(url,data, {
        headers: { "Content-Type": "application/json" },
    })
    .then((data) => {
        console.log(data.data)
        res.send(JSON.stringify({"data":data.data}))
    });
})

module.exports = router