const express = require('express');
const cors = require('cors');
const pool = require('./db');

const app = express();

app.use(cors());
app.use(express.json());
app.use(express.static('../frontend'));


// LOGIN
app.post('/login', async(req,res)=>{

    const {username,password} = req.body;

    const result = await pool.query(
        'SELECT * FROM users WHERE username=$1 AND password=$2',
        [username,password]
    );

    if(result.rows.length > 0){
        res.json(result.rows[0]);
    }else{
        res.json({error:"Wrong login"});
    }
});


// GET PEOPLE
app.get('/people', async(req,res)=>{
    const result = await pool.query('SELECT * FROM people ORDER BY id DESC');
    res.json(result.rows);
});


// ADD PERSON
app.post('/people', async(req,res)=>{

    const {fullname,photo,position,ministry,start_date,end_date} = req.body;

    await pool.query(`
        INSERT INTO people(fullname,photo,position,ministry,start_date,end_date)
        VALUES($1,$2,$3,$4,$5,$6)
    `,[fullname,photo,position,ministry,start_date,end_date]);

    res.json({message:"added"});
});



// DELETE
app.delete('/people/:id', async(req,res)=>{

    await pool.query(
        'DELETE FROM people WHERE id=$1',
        [req.params.id]
    );

    res.json({message:"deleted"});
});

app.listen(3000,()=>{
    console.log("Server running on 3000");
});

app.listen('/people/:id', async(req,res)=>{
    await pool.query(
        'listen all from people',
        [req.params.id]
    );
    res.json({message:"deleted"});
});

app.listen(3000,()=>{
    console.log("Server running on 3000");
});


