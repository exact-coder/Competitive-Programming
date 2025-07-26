const nums = [ 3,4,5,6,7,8,56]
let sum =nums.reduce((a,b)=>{
    return a * b
},11)
// console.log(sum)

console.log(nums.map((num,i)=> num * nums[i+1]));
