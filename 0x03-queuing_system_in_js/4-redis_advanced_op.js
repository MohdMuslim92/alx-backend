import redis from 'redis';

// Create a Redis client
const client = redis.createClient(6379, '127.0.0.1');

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Create Hash
function createHash (hashName, hashValues) {
  Object.entries(hashValues).forEach(([key, value]) => {
    client.hset(hashName, key, value, redis.print);
  });
}

// Display Hash
function displayHash (hashName) {
  client.hgetall(hashName, (err, reply) => {
    if (err) {
      console.error(`Error getting ${hashName} hash: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Call functions to create and display hash
createHash('HolbertonSchools', {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
});

displayHash('HolbertonSchools');

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully close the connection on process termination
process.on('SIGINT', () => {
  client.quit();
});
