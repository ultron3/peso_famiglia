let msg = 'ciao';

const pi=3.14; 

if (msg === 'ciao'){
    alert('collegamento a mongodb effettuato ');
}else{
    alert('il messaggio non contiene ciao');
}






var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("dbmpalestra");
  dbo.createCollection("customers", function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
    db.close();
  });
});