// Node Redis client and async operations

import { promisify } from 'util';
import redis from 'redis';

const client = redis.createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
}

const displayAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  try {
    const val = await displayAsync(schoolName);
    console.log(`${val}`);
  } catch (err) {
    console.error(`Error: ${err}`);
  }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
