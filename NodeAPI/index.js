const express = require('express')
const app = express()

const port =process.env.PORT || 3000;

app.get('/',(req,res)=>{
    res.send("Hello worlds");
});

app.set('port', process.env.PORT || 3000);

app.listen(port,()=>
console.log(`Express webb app available at http://localhost:${port}`)
);