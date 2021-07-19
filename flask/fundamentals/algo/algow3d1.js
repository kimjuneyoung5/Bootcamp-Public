const nums1 = [1,2,3,4,10]
const expected1 = true
const nums2 = [1,2,4,2,1]
const expected2 = false

function balancePoint(nums){
  let leftSum = 0
  let rightSum = 0
  
  for(let i = 0; i<nums.length-1; i++){
    for(let j = i+1; j<nums.length; j++){
      rightSum += nums[j]
    }
    leftSum+=nums[i]
    if (leftSum == rightSum){
      return true
    }
    rightSum = 0
  }
  return false
}

console.log(balancePoint(nums1))
console.log(balancePoint(nums2))

const nums1 = [-2, 5, 7, 0, 3]
const expected1 = 2
const nums2 = [9, 9]
const expected2 = -1

function balanceIndex(nums){
  let leftSum = 0
  let rightSum = 0
  
  for(let i = 1; i<nums.length; i++){
    leftSum += nums[i-1]
    for(let j = i; j<nums.length; j++){
      if(j != i){
        rightSum += nums[j]
      }
      if(leftSum == rightSum){
        return i
      }
    }
    rightSum = 0
  }
  return -1
}

console.log(balanceIndex(nums1))
console.log(balanceIndex(nums2))