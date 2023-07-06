function hola(nombre){
    return new Promise(function(resolve,reject){
        setTimeout(function(){
            console.log('hola '+nombre);
            resolve(nombre)
            reject('hay un error...')
        }, 1000)
    })
}

function hablar(nombre){
    return new Promise((res,rej)=>{
        console.log('como estas '+nombre)
        res(nombre);
        rej('note entiendo ...')
    })
}

let nom = 'Cesar';


hola(nom)
    .then(hablar)
    .then((nom)=> console.log('adios '+ nom))