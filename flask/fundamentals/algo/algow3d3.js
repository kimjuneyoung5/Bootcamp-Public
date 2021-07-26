const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

function dedupeSorted(nums) {
  var arr = []
  for(var i = 0; i < nums.length; i++){
    if(arr.includes(nums[i]) === false){
      arr.push(nums[i])
    }
  }
  return arr
}

console.log(dedupeSorted(nums1))
console.log(dedupeSorted(nums2))
console.log(dedupeSorted(nums3))

const nums1 = [];
const nums2 = [1];
const nums3 = [5, 1, 4];
const nums4 = [5, 1, 4, 1];
const nums5 = [5, 1, 4, 1, 5];

function mode(nums) {
    var arr = []
    if(nums.length < 1){
      return []
    }
    else if(nums.length == 1){
      arr.push(nums[0])
      return arr
    }
    var count_arr = []
    var max_count = 1
    var arr = dedupeSorted(nums)
    for(var i = 0; i < arr.length; i++){
      var count = 1
      for(var j = 0; j < nums.length; j++){
        if(nums[i] == nums[j]){
          count++
        }
      }
      count_arr.push(count)
    }
    new_arr = []
    for(var k = 0; k<count_arr.length; k++){
      if(count_arr[k] > max_count){
        max_count = count_arr[k]
      }
    }
    for(var a = 0; a < count_arr.length; a++){
      if(max_count == count_arr[a]){
        new_arr.push(arr[a])
      }
    }
    return new_arr
}


function mode(nums) {
    if (nums.length === 1) {
      return [nums[0]];
    }
  
    const modes = [];
    const freq = {};
    let maxFreq = 0;
    let allSameFreq = true;
  
    for (const n of nums) {
      freq.hasOwnProperty(n) ? freq[n]++ : (freq[n] = 1);
  
      if (freq[n] > maxFreq) {
        maxFreq = freq[n];
      }
    }
  
    for (const key in freq) {
      if (freq[key] === maxFreq) {
        // keys are strings, convert back to int
        modes.push(parseInt(key));
      } else {
        allSameFreq = false;
      }
    }
    // return empty array if allSameFreq, else return modes
    return allSameFreq ? [] : modes;
  }
console.log(mode(nums1))
console.log(mode(nums2))
console.log(mode(nums3))
console.log(mode(nums4))
console.log(mode(nums5))