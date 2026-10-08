let age = 44
const my_name = 'Denis'
console.log(my_name)

// условия
if(age < 55){
console.log(age,' Меньше')
} else {
console.log(age,' Больше')
}

// обычные функции
function doIt() {
console.log('Привет функция doIt')
}

// стрелочные функции
const arrow = (name) => {
console.log(name)
};

arrow(my_name)

// цикл for
for(let x = 0;x <= 7;x++){
    console.log(x)
}

// цикл while
let p = 1
while (p < 5){
    console.log(x)
    p++
}

// массивы
let numbers = [1,2,3,4,5]
// объект
let pet = {
    name:'cat',
    age:10
}

console.log(pet.name)