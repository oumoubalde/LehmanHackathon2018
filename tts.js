const express = require("express");
const app = express();
const fs = require("fs");

app.get("/", (req, res)=>{
    fs.readFile("./textToSpeech.txt",'utf-8', (err, data)=>{
    if(err) throw err;
    res.send("<h1 style='color:red; font-weight:bold;text-align:center'>" + data + "</h1>");
})
})

app.listen(8080);

