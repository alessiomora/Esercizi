const http = require('http');

setTimeout(() => {
  http.get('http://server:80/', (res) => {
    let data = '';

    res.on('data', chunk => data += chunk);
    res.on('end', () => {
      console.log(JSON.parse(data));
    });
  }).on('error', (err) => {
    console.error('Errore:', err.message);
  });
}, 5000);
