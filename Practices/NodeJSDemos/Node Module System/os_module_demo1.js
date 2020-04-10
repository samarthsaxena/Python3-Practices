const os = require('os');

var totalmemory = os.totalmem();
var freeMemory = os.freemem();

console.log('Total memory: '+ totalmemory);

//Template string as per ES2015
console.log(`Total memory : ${totalmemory}`);
console.log(`Free memory : ${freeMemory}`);
