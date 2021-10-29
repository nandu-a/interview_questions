let n = 5;

function fizzbuzz(n) {
  let arr = [];
  if (n % 15 === 0) {
    arr.push("fizzbuzz");
  } else if (n % 3 === 0) {
    arr.push("fizz");
  } else if (n % 5 === 0) {
    arr.push("buzz");
  } else {
    arr.push(n);
  }
  return arr
}