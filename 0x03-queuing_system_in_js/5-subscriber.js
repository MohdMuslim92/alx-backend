// Import necessary modules
import redis from 'redis';

// Create a Redis client
const subscriber = redis.createClient(6379, '127.0.0.1');

// Event handler for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the holberton school channel
subscriber.subscribe('holberton school channel');

// Event handler for received messages
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit if message is KILL_SERVER
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
