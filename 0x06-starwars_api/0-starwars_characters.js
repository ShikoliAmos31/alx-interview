#!/usr/bin/node
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL to fetch the movie data from the Star Wars API
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make the HTTP GET request to the Star Wars API
request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Failed to get data. Status code:', response.statusCode);
    return;
  }

  const data = JSON.parse(body);
  const characters = data.characters;

  // Fetch all character data in parallel, but print them in the correct order
  const characterPromises = characters.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
        } else if (charResponse.statusCode !== 200) {
          reject(new Error('Failed to get character data'));
        } else {
          resolve(JSON.parse(charBody).name);
        }
      });
    });
  });

  // Wait for all promises to resolve and then print the character names in order
  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => console.error('Error:', error));
});
