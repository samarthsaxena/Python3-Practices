//we use require() function for importing a module

//since this is in same directory we use a period and / then the name of js file
//Node knows that this is the js file so,
//optionaly we can mention the below line as require('./logger_module.js');
// var logmodule = require('./logger_module');

//Standard coding practice is to store the returned value of require() function
//in const type
//So that it can not be over-riden by any other modifications on the variable
const log = require('./logger_module');
//If any thing is trying to modify this
//error would be thrown
//Since it is a constanst value

//o/p: { log_funtion: [Function: log] }
console.log(log);


//this is from the module you imported
log("From imoprting module js file using the exported function of logger_module.js");
