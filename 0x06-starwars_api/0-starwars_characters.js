#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (err, res, body) => {
  if (err) { console.error(err); } else if (res.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;
    characters.forEach(
      characterurl => {
        request(characterurl, (err, res, body) => {
          if (err) {
            console.error(err);
          } else if (res.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      }
    );
  }
});
