// Track progress and errors with Kue: Create the Job processor

import { createQueue } from 'kue';
const queue = createQueue();

const blacklisted = [ '4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0);
  if (blacklisted.includes(phoneNumber)) {
    const errMes = `Phone number ${phoneNumber} is blacklisted`
    done(new Error(errMes));
  } else {
    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
