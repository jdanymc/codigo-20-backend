const express = require("express");

const app = express();

/******* MIDDLEWARES********* */
// de aplicacion

app.use(function (req, res, next) {
  console.log("esto es un middleware");
  console.log("request method", req.method);
  next();
});

app.use((req, res, next) => {
  const timeElapsed = Date.now();
  const today = new Date(timeElapsed);

  console.log("ejecutado a las ", today.toISOString());
  next();
});

//middleware de ruta
app.use("/usuario", (req, res, next) => {
  console.log(a+3);
  console.log("request url :",req.originalUrl);
  next();
});

/**************************** */

app.get("/", (req, res) => {
  res.json({
    status: true,
    content: "ejemplos de middlewares",
  });
});

app.get("/usuario", (req, res) => {
  res.json({
    nombre: "admin",
    email: "admin@mail.com",
  });
});

//middlewares de errores
app.use((err,req,res,next)=>{
  console.error(err.stack);
  res.status(500).json({
    status:false,
    content:'ocurrio un error inesperado'
  })
})



app.listen(5001, () => console.log("http"));
