// Tests for createPushNotificationsJobs function

import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';
import { createQueue } from 'kue';

describe('test for job creation', () => {
  let queue;

  before(() => {
    queue = createQueue();

    if (typeof queue.testMode === 'function') {
      queue.testMode(true);
    }
  });

  after(() => {
    if (typeof queue.testMode === 'function') {
      queue.testMode(false);
    }
  });

  it('should display an error message if jobs is not an array', () => {
    const jobs = {
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account',
    };

    const testFunc = () => createPushNotificationsJobs(jobs, queue);

    expect(testFunc).to.throw(Error, 'Jobs is not an array');

    if (typeof queue.testMode === 'function') {
      expect(queue.testMode.jobs.length).to.equal(0);
    }
  })

  it('create jobs in queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    createPushNotificationsJobs(list, queue);

    if (typeof queue.testMode === 'function') {
      expect(queue.testMode.list.length).to.equal(list.length);
    }
  });
});
