#!/usr/bin/node
// Get the names of characters in a film
const request = require('request');
const util = require('util');

const get = util.promisify(request.get);

const getFilmData = async (filmUrl) => {
  const response = await get(filmUrl);
  const results = JSON.parse(response.body);
  return results;
};

const getUserData = async (userUrl) => {
  const response = await get(userUrl);
  const userResults = JSON.parse(response.body);
  return userResults;
};

const main = async () => {
  try {
    const id = process.argv[2];
    const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + id;
    const filmData = await getFilmData(filmUrl);
    for (let index = 0; index < filmData.characters.length; index++) {
      const userUrl = filmData.characters[index];
      const userData = await getUserData(userUrl);
      console.log(userData.name);
    }
  } catch (error) {
    console.error(error);
  }
};

main();
