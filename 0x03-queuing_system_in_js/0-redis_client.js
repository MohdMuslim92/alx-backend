// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient(6379, '127.0.0.1');

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully close the connection on process termination
process.on('SIGINT', () => {
  client.quit();
});
