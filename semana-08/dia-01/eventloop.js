/*console.log("paso 1");
console.log("paso 2");
console.log("paso 3");*/

/*console.log("paso 1");
for(i=1;i<=5;i++)
    console.log("paso "+i);*/

let i  = 0;
let id = setInterval(function(){
    i++;
    if(i===5){
        clearInterval(id)
    }
    console.log("paso "+i)
},1000)

console.log("Fin")