let customers = [
  { id: 0, name: 'paul' },
  { id: 1, name: 'jeff' },
  { id: 2, name: 'mary' }
];
let customer = customers.find(cust => cust.name === 'jeff');
console.log(customer);
