// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient(6379, '127.0.0.1');

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

// Function to display the value for a school key in Redis
function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error getting ${schoolName} value: ${err}`);
    } else {
      console.log(`${schoolName}: ${reply}`);
    }
  });
}

// Calling the functions as per the requirements
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100', () => {
  displaySchoolValue('HolbertonSanFrancisco');
});

// Event handler for connection errors
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Gracefully close the connection on process termination
process.on('SIGINT', () => {
  client.quit();
});
