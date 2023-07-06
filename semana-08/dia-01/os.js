const os = require('os')

const procesador = os.arch()
const sistema = os.platform()
const cpu = os.cpus().length
const memoria = os.totalmem()

console.log('procesador '+procesador);
console.log('sistema operativo ' + sistema);
console.log('CPU ' + cpu);
console.log('Memoria RAM ' + memoria/(1024*1024*1024));

function calcularMemoria(capacidad, tipo){
    return new Promise((res,rej)=>{
        let memoria_convertida = capacidad/1024
        console.log('MEMORIA EN '+ tipo +':'+ memoria_convertida)     
        res(memoria_convertida)   
    })
}

console.log('======= MEMORIA CON PROMESAS=========')

calcularMemoria(os.totalmem(),'KB')
.then((kb)=>calcularMemoria(kb,'MB'))
.then((mb)=>calcularMemoria(mb,'MB'))