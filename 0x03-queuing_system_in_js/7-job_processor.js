// Import the necessary modules
const kue = require('kue');

// Define the blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification (phoneNumber, message, job, done) {
  // Track the progress of the job
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job with an error message
    job.failed(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return done();
  }

  // Update the job progress
  job.progress(50, 100);

  // Log the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

// Create a queue with Kue
const queue = kue.createQueue();

// Process jobs from the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job details and completion callback
  sendNotification(phoneNumber, message, job, done);
});
