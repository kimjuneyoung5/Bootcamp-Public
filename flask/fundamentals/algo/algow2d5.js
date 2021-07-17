const strA1 = "yes";
const strB1 = "eys";

const strA2 = "yes";
const strB2 = "eYs";
const expected2 = true;

const strA3 = "no";
const strB3 = "noo";

const strA4 = "silent";
const strB4 = "listen";

function isAnagram(s1, s2) {
  var arr = s1.split("");
  var count = 0;
  var s3 = s2.toLowerCase()
  if( s1.length != s2.length ){
    return false;
  }
  for(var i =0; i<s1.length; i++){
    if(s3.includes(arr[i])){
      count++;
    }
    else{
      return false;
    }
  }
  return true;
}
console.log(isAnagram(strA1,strB1))
console.log(isAnagram(strA2,strB2))
console.log(isAnagram(strA3,strB3))
console.log(isAnagram(strA4,strB4))

const str1 = "   hello world     ";
const expected1 = "hello world";

function trim(str) {
  var first_index = 0;
  var last_index = 0;
  var newText = ""
  for(var i = 0; i <str.length; i++){
    if(str[i] != " "){
      first_index = i;
      i = str.length;
    }
  }
  for(var j = str.length-1; j > 0; j--){
    if(str[j] != " "){
      last_index = j;
      j = str.length;
    }
  }
  for(var k = first_index; k < last_index+1; k++){
    newText += str[k];
  }
  return newText;
}
console.log(trim(str1))