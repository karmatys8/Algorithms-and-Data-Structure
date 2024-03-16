// given arrays A and B, containing numbers
// return from A only those that appear non-prime number of times in B
// order should be maintained


// time complexity:
// O(b + b * log(log b) + a) = O(max(a, b * log(log b)))
// where: a - length of A, b - length of B

const getSieve = (n) => {
  let array = new Array(n + 1).fill(true);
  array[0] = array[1] = false;

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (array[i]) {
      for (let j = 2 * i; j <= n; j += i) {
        array[j] = false;
      }
    }
  }

  return array;
};

const solution = (A, B) => {
  const map = new Map();
  let mostCommonCnt = 0;

  for (const element of B) {
    // if element is not yet in map, prev should be 0
    const prev = map.get(element) || 0;
    const curr = prev + 1;

    map.set(element, curr);
    mostCommonCnt = Math.max(mostCommonCnt, curr);
  }

  const sieve = getSieve(mostCommonCnt);

  const result = [];
  for (const element of A) {
    // map.get(element) returns the amount of occurrences of element in B
    // then we check if this value is (false in our sieve === not prime)
    if (!sieve[map.get(element)]) {
      result.push(element);
    }
  }

  return result;
};
