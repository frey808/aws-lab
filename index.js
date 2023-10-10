// static database manipulation and testing
require('dotenv').config()
const mysql = require('mysql2')
const connection = mysql.createConnection(process.env.DATABASE_URL)
connection.query('SHOW TABLES', function(err, results){console.log(results)})
connection.query('SELECT * FROM items', function(err, results){console.log(results)})
// connection.query('CREATE TABLE items(id SERIAL PRIMARY KEY, name VARCHAR(31))', function(err, results){console.log(results)})
// connection.query('DROP TABLE IF EXISTS items', function(err, results){console.log(results)})
// connection.query('INSERT INTO items (id, name) VALUES (1, "test item")', function(err, results){console.log(results)})
connection.end()

function openNav(){
    document.getElementById("nav").style.display = "inline";
    document.getElementById("opennav").style.display = "none";
}

function closeNav(){
    document.getElementById("nav").style.display = "none";
    document.getElementById("opennav").style.display = "inline";
}

function swap(){
    //swap view
}

function getData(){
    const connection = mysql.createConnection(process.env.DATABASE_URL)
    connection.query('SELECT * FROM items', function (err, results) {
        document.getElementById("test").innerHTML = results;
    })
    connection.end()
}

function createItem(){
    //add
}

function editItem(){
    //edit
}

function deleteItem(){
    //delete
}