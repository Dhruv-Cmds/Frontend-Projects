// 1. Crate a variable of type string and try to add a number to it,

let a = "I'm a string";
let b = 30;

console.log(a + b);

{
    let a = "20";
    let b = 30;

    console.log(a + b)
}

// It won't work Just add to next to each other.

// 2. Use typeof operator to find the datatype of the string in last question,

console.log(typeof a, typeof b)

// a is string and b is number.

// 3. Create a const object in JavaScript can change it to hold a number later?,

const d = {"name": "dhruv"};
console.log(d)

// You cant assign or increase anything later to any const defined value.

// 4. Try to add a new key to the const object in problem 3,

// d = {"role": "admin"};
// console.log(d);

// You cant rechange assign to any const value.

// Write a JavaScript program to create a word meaning directorty of 5 words.

let dictionary = {
    apple: "A fruit",
    book: "A collection of pages",
    computer: "An electronic machine",
    chair: "A piece of furniture to sit on",
    sun: "The star at the center of our solar system"
}

console.log(dictionary);
console.log(dictionary.sun)