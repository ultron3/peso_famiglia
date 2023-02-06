async function getData() {
  return Promise.resolve('data');
}

async function getMoreData(data) {
  return Promise.resolve(data + 'more data');
}

async function getAll() {
  const data = await getData();
  const moreData = await getMoreData(data);
  return `All the data: ${data}, ${moreData}`;
}

getAll().then((all) => {
  console.log('all the data')
})


var http = require('http');

//create a server object:
http.createServer(function (req, res) {
  res.write('Hello World!'); //write a response to the client
  res.end(); //end the response
}).listen(8080); //the server object listens on port 8080