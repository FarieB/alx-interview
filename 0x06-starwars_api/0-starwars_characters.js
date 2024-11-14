#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const filmEndPoint = `https://swapi-api.hbtn.io/api/films/${movieId}`;
let characters = [];

const fetchJSON = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err || res.statusCode !== 200) {
        reject(`Error: ${err} | StatusCode: ${res.statusCode}`);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const printCharacterNames = async () => {
  try {
    const movieData = await fetchJSON(filmEndPoint);
    characters = movieData.characters;

    for (const characterURL of characters) {
      const characterData = await fetchJSON(characterURL);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error(error);
  }
};

printCharacterNames();
