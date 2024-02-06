// Import necessary modules
import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient(6379, '127.0.0.1');

// Promisify the client.get function
const asyncGet = promisify(client.get).bind(client);

// Event handler for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Function to set a new school value in Redis
function setNewSchool (schoolName, value, callback) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error(`Error setting ${schoolName} value: ${err}`);
    } else {
      console.log(`${schoolName}`);
      redis.print(reply);
      console.log(`${value}`);
      callback(); // Call the callback once the operation is complete
    }
  });
}

// Function to display the value for a school key in Redis using async/await
async function displaySchoolValue (schoolName) {
  try {
    const value = await asyncGet(schoolName);
    console.log(`${schoolName}: ${value}`);
  } catch (error) {
    console.error(`Error getting ${schoolName} value: ${error}`);
  }
}

// Calling the functions as per the requirements
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100', async () => {
  await displaySchoolValue('HolbertonSanFrancisco');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully close the connection on process termination
process.on('SIGINT', () => {
  client.quit();
});
