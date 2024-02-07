// Import the necessary modules
import kue from 'kue';

// Define the function to create push notification jobs
function createPushNotificationsJobs (jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Loop through each job in the array
  jobs.forEach((jobData) => {
    // Create a new job in the queue
    const job = queue.create('push_notification_code_3', jobData);

    // Log when a job is created
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Log when a job is completed
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Log when a job fails
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    });

    // Log job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

// Export the function
export default createPushNotificationsJobs;
