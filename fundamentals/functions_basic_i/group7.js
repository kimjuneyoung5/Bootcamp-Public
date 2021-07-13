/* 
	Acronyms
	Create a function that, given a string, returns the string’s acronym 
	(first letter of each word capitalized). 
	Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

function acronymize(str) {
	var wordsArr = str.split(" ")
	var arr = []
	for( var i = 0; i < wordsArr.length; i++){
		var acr = wordsArr[i].split('')
		arr.push(acr[0])
	}
	console.log(arr.join('').toUpperCase())
} 
acronymize(str1)

const str1 = " there's no free lunch - gotta pay yer way. ";
const str2 = "Live from New York, it's Saturday Night!";
function acro(str) {
    var arr = " "
	if (str[0] != " "){

	}
    for( var i = 0; i < str.length; i++){
        if(str[i] == " " && str[i+1] != null){
            arr += str[i+1]
        }
    }
    console.log(arr.toUpperCase())
}
acro(str1)
acro(str2)
/*****************************************************************************/

/* 
	String: Reverse
	Given a string,
	return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverseString(str) {
    var arr = " "
	for( var i = str.length - 1 ; i > -1 ; i-- ){
		arr += str[i]
	}
    console.log(arr)
}
reverseString(str1)
reverseString(str2)

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

function reverse(str){
	str = str.trim();
	var wordsArr = str.split("")
	var temp;
	str = " "
	var last = wordsArr.length - 1
	for(var i = 0; i< wordsArr.length/2; i++){
		temp = wordsArr[i]
		wordsArr[i] = wordsArr[last]
		wordsArr[last] = temp
		last--
	}
	console.log(wordsArr.join(''))
}
reverse(str1)