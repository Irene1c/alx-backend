// Creating the Job creator with `kue`

import { createQueue } from 'kue';
const queue = createQueue();

const job = queue.create('push_notification_code', {
  phoneNumber: '12345',
  message: 'notification',
});

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

job.save();
