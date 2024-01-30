#!/usr/bin/node

const request = require('request');

request('https://swapi.dev/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    return console.log(error);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        return console.log(charError);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
