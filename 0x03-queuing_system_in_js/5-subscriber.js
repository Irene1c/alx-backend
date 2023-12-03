// Node Redis Client subscriber

import { createClient } from 'redis';

const client = createClient();

client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
  }
  if (message === 'KILL_SERVER') {
    client.unsubscribe(channel);
    client.quit();
  }
});
