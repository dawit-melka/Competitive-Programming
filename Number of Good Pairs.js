var numIdenticalPairs = function(nums) {
  let obj = {};
  let count = 0;
  for (let n of nums) {
    if (obj[n]) {
      count += obj[n];
      obj[n] = obj[n] + 1;
    } else obj[n] = 1;
  }
  return count;
};
