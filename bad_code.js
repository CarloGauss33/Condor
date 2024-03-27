function add(num1, num2) {
    if (typeof num1 == 'number' && typeof num2 == 'number') {
      return num1 + num2;
    } else {
      return 'Error: Both inputs must be numbers';
    }
  }
  
  console.log(add(1, '2')); // This will return 'Error: Both inputs must be numbers'
