import kue from 'kue';

// Create a queue
const queue = kue.createQueue();

// Define job data
const jobData = {
  phoneNumber: '123456789',
  message: 'Hello, this is a notification message.'
};

// Create a job
const job = queue.create('push_notification_code', jobData);

// Event handler for successful job creation
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event handler for failed job
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});
