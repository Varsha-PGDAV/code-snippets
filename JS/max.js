let data = [1,2,3,4,5];
console.log(...data);
let data2 = [6,7,8,9,10];
let combined = [...data, ...data2];
console.log(...combined);
console.log(Math.max(...combined));
