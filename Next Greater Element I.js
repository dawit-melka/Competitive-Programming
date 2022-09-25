var nextGreaterElement = function(nums1, nums2) {
  const map = {};
  const stack = [];
  nums2.forEach(n => {
    while (stack.length > 0 && stack[stack.length - 1] < n) {
      map[stack.pop()] = n;
    }
    stack.push(n);
  });
  return nums1.map(n => map[n] || -1);
};
