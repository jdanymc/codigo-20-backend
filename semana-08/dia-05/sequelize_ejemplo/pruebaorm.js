const Sequelize = require('sequelize')

const sequelize = new Sequelize({
    dialect : 'sqlite',
    storage : './database.sqlite'
})

sequelize.authenticate()
.then(()=>console.log("base de datos creada con exito"))
.catch(err=>console.log('error: ' + err))

//crear modelo

const Alumno = sequelize.define(
    'tbl_alumno',
    {
        nombre:Sequelize.STRING,
        email:Sequelize.STRING
    },{// para retirar campos adicionales
        freezeTableName:true,
        timestamps:false
    }
)

//migraciones

sequelize.sync()
.then(()=>{
    console.log('migracion exitosa');
    Alumno.bulkCreate(
        [
            {nombre:'Cesar Mayta',email:'cesar@mail.com'},
            {nombre:'Claudia Paz',email:'claudia@mail.com'},

        ]
    ).then(()=>{
        return Alumno.findAll()
    }).then((alumnos)=>console.log(alumnos))
})