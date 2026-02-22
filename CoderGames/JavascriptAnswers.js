// 1.) Declare a variable and assign it to an integer, then output the number raised to the power of 3.
let n = 2;
console.log(n**3); //exponent

// 2.) Declare a variable and assign it to the list [1,2,3,4,5]. Calculate then output the sum of the list.
let q = [1,2,3,4,5]
let o = 0
for(let i = 0; i<5; i++){
  o += q[i]
  //console.log(q[i])
}
console.log(o)

//3.) Print the numbers from 1 to 100 and skip anything that is divisible by 9.
for (let i = 1; i<=100; i++){
  //% = mod = gives me remainder
  if (i%9 !=0){
    console.log(i);
  }
}


//5.) Declare a variable and assign it to any number, and output the last digit of the number. Input 2345 would output 5, while 9876 would output 6.
let a = 217;
a = a.toString()
// .length = gives us the length of a string or an array
console.log(a[a.length-1])


//4.) Declare a variable and assign it to ”Programming isn't about what you know; it's about what you can figure out.” then calculate the count of the number of words in the variable and output the number.
let b = "Programming isn't about what you know; it's about what you can figure out."
//split() - take a string and split it by a seperator
let wordsList = b.split(" ");
console.log(wordsList.length);


//.6) Declare a variable and assign it to a string value. 
// Then output the string where each letter in the word must be one of these characters: 't', 'u', 'r', 'i', 'n', 'g'. Otherwise omit that letter. An example would be: 'fun rigid' would output: 'unrigi'.
let sentence = "Aayana is amazing" 
let letters = ['t', 'u', 'r', 'i', 'n', 'g']
for (let character of sentence){
  for (let c of letters){
    if (character.toLowerCase() == c){
      console.log(character)
    }
    
  }
}

//7.) Declare a variable and assign it to the list [1,2,3,4,5]. Calculate then output the list in reverse order. We will be changing the values when grading.

let seven = [1,2,3,4,5,6]
let ans = []
for (let i = seven.length-1; i > -1;i--  ){
  ans.push(seven[i])//push = add
}
console.log(ans)

//8.) Declare a variable and assign it to a string ”seven”. Output the string with 1 of the first letter followed by 2 of the second letter followed by 3 of the third letter and so on. We will be changing the values when grading.

//seevvveeeennnnn
let eight = "seven";
let count = 1;
for (let character of eight){
  console.log(character.repeat(count))
  count++;
  
}
