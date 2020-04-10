    // var x = ;
    var url = "http://mylogger.io";
    console.log('__filename: '+__filename);
    console.log('__dirname: '+__dirname)

    function log(message) {
      //Send  an HttpReq. that can be logged
      console.log(message);
    }

    //exporting anything from this file makes it available for others to use.
    //Remeber there was a property called exports??
    //try console.log(module); you'd see the property
    //that's where we're making this logger function as log_funtion available.

    //If an object has to be exported we use below syntaxt
    // module.exports.log_funtion = log;

    //If we need to export only few things like variables of functions we can go for below syntax
    module.exports = log
