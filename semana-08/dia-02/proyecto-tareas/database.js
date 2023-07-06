const mysql = require('mysql')
// const mysql = require('mysql2')  // si se instala el mysql2

const mysqlConnection = mysql.createConnection({
    host:'localhost',
    user:'root',
    password:'',
    database:'db_tareas_g20'
})
/*
si da error en autenthicacion ejecutar(lo recomendable es usar mysql2):

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
FLUSH PRIVILEGES;
*/
mysqlConnection.connect(function(err){
    if(err){
        console.error(err);
        return
    }
    else{
        console.log('conectado a bd');
    }
})

module.exports = mysqlConnection