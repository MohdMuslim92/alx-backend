import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  let queue;

  // Before running tests, create a queue and enter test mode
  before(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  // After running tests, clear the queue and exit test mode
  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('create two new jobs to the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Validate the number of jobs in the queue
    expect(queue.testMode.jobs.length).to.equal(2);

    // Validate job data
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
