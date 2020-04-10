const fs = require('fs');

fs.readdir('./', function(err, fileNames) {

if (err) console.log('Error: ',err);
else {
  console.log('Files:',fileNames);
  console.log('Total number of files: ',fileNames.length)

}

});
