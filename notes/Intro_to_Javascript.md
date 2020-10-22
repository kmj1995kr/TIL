## Intro to Javascript

A typical Javascript function is structured like:

`function add (x, y) { return x + y; }`

`function`: keyword

`add`: function name

`(x,y)`: parameters

`{ return x + y; }`: function body



### Ways of Declaring a Function

**Function Expression**: defining a function, then assigning the function to a variable

- **Anonymous Function**: declaring a function but not specifying the name of the function (instead just assigning the function to a var)
  - More common form of the function
- **Named Function**: naming the function itself
  - Cannot be used externally
  - Can used to call itself in a recursive manner

```javascript
//Anonymous Function
var add = function(x, y) {
    return x + y;
};

//Named Function
var myFactorial = function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n-1);
}
```



**Function Declarations**: declaring a function without assigning to a variable

```javascript
function add(x, y) {
    return x + y;
};

// In Javascript, this is still processed as var add = function add(x, y) { return x + y };
```



**Using Function()**

```javascript
var add = new Function('x', 'y', 'return x + y');
```



### Types of Functions

**Callback Function**: When a certain events(actions) happen, the function is called

- Ex. Event handler
- It's usually used as a parameter in another function

**Immediate Function**: Functions that are executed as they are defined

- Functions that only need to be run once in the entire script
- Function is wrapped in parenthesis

```javascript
(function (x, y) {
    console.log(x + y);
})(3, 4);
```



**Inner Function:** Functions that can utilize the information in the parent function, but cannot be used outside of the function

```javascript
function parent() {
    var a = 100;
    var b = 200;
 
    function child() {
        var b = 300;
 
        console.log(a);     // 100
        console.log(b);     // 300
    };
}
 
parent();
child();                    // child is not defined
```



**Function that Returns Itself** (also a part of an inner function)

```javascript
var self = function() {
    console.log('a');
    
    return function() {
        console.log('b');
    };
};
//only prints a
self();
console.log('-------------')
//prints both a and b
self = self(); // a
self();  // b -- closure https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures
```



### Characteristics of Javascript

- Functions can be created as a value --> functions can be stored in a variable

  - `var add = function(x, y) { return x + y }`

- It's a good practice to put ; at the end of each statement

  ```javascript
  var x = 1;
  var y = 2;
  
  var add = function(x, y) {
      return x + y;
  };
  
  console.log(add(3,4));
  ```

- **Function Hoisting**: technique that moves function declaration to the top of their scope before any other code execution. No matter where the function is declared, it is still applied to the entire script.
  - This happens because variable instantiation and initialization is done separately
  - If a function is "declared", then it is hoisted throughout the document
  - If a function is "assigned to a variable in an expression", then the order does matter

  ```javascript
  console.log(add(1,2)); // 3
  
  function add(x, y) {
      return x + y;
  }
  
  console.log(add(3,4)); // 7
  ```

  ```javascript
  console.log(x); // undefined because x is instantiated, but a value of 2 is not initialized to the variable
  var x = 2		
  console.log(x); // 2
  
  console.log(y); // y is not defined
  
  var z; 
  console.log(z); // undefined
  ```

- **Arguments Object**: parameters saved in a list form

  - When a function is called, an arguments object is automatically created with the parameters
    - When there is exactly same amount of parameters --> returns the function
    - When there's more parameters than defined --> ignores later parameters
    - When there's less parameters than defined --> NaN
  - Can be used to create functions that have unknown number of parameters

  ```javascript
  function sum() {
      var result = 0;
      for (var i = 0; i < arguments.length; i ++) {
          result += arguments[i];
      }
      return result;
  }
  console.log(sum(1)); //1
  console.log(sum(1, 2)); //3
  console.log(sum(1, 2, 3)); //6
  ```



- **this**: Stores value of the parameters and arguments of the object

  - Depending on how the function is called, it references different values from the object

  ```javascript
  var myObj = {
      name: 'minnczi',
      sayName: function() {
          console.log(this.name)
      }
  };
  
  var otherObj = {
      name: 'other'
  }
  
  otherObj.sayname = myObj.sayName;
  
  myObj.sayname(); // minnczi
  otherObj.sayname(); // other
  ```

  

  ```javascript
  var text = "This is JavaScript";
  console.log(text);          // This is JavaScript
  console.log(window.text);   // This is JavaScript
  console.dir(window);
   
  var say = function() {
      console.log(this);      // Window {window: Window, self: Window, document: document, name: "", location: Location, …}
      console.log(this.text); // This is JavaScript
  };
  say();
  ```

  
  - `this` in the inner function binds to the global value

  ```javascript
  var value = 100;
   
  var myObject = {
      value: 1,
      func1: function() {
          this.value += 1;
          console.log(`func1() called. this.value = ${this.value}`);          // #1 2
   
          func2 = function() {
              this.value += 1;
              console.log(`func2() called. this.value = ${this.value}`);      // 101
   
              func3 = function() {
                  this.value += 1;
                  console.log(`func3() called. this.value = ${this.value}`);  // 102
              }
              func3();
          }
          func2();
      }
  };
  myObject.func1();
  ```

  - If we want the inner functions to reference to the value inside the function (instead of a global variable), then we can use the variable `that` or `_this` to store the value of `this`

  ```javascript
  var value = 100;
   
  var myObject = {
      value: 1,
      func1: function() {
          var that = this;
          this.value += 1;    
          console.log(`func1() called. this.value = ${this.value}`);          // 2
   
          func2 = function() {
              that.value += 1;
              console.log(`func2() called. this.value = ${that.value}`);      // 3
   
              func3 = function() {
                  that.value += 1;
                  console.log(`func3() called. this.value = ${that.value}`);  // 4
              }
              func3();
          }
          func2();
      }
  };
  myObject.func1();
  ```

- **Undefined values**

  - Variables that are declared, but doesn't have any assigned value 
  - ex. `var x`
  - Undefined variables are neither true or false

- In Javascript, to determined if the value is undefined or not, `!` is used

  - `x = !x` : if a value is true, x is true, if a value is false, x is false
  - `x = !!x`: if a value is true, x is true, if a value is false or undefined, x is false
  - `x = !!x` is normally used to determined if the parameter is undefined

### Using jQuery

**Basic Syntax**

```javascript
windows.onload = () => {
        console.log("#1");
};

jQuery(document).ready(function() {
    console.log("#2");
});

$(document).ready(function() {
    console.log("#3");
});

jQuery(function() {
    console.log("#4");
});

$(function() {
    console.log("#5");
})
```

