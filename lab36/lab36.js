<!DOCTYPE html>
<html>
<head>
    <title>JS Functions & Scope</title>
</head>
<body>

<h2>JavaScript Functions & Scope</h2>

<script>
    // Lab 1: Creating Functions

    // Function keyword
    function sum(a, b) {
        return a + b;
    }
    console.log("Sum:", sum(5, 3));

    // Arrow function
    const square = (num) => num * num;
    console.log("Square:", square(4));

    // Function expression
    const max = function(a, b) {
        return (a > b) ? a : b;
    };
    console.log("Larger number:", max(10, 20));


    // Lab 2: Global vs Local Scope
    let message = "Hello from global";

    function showMessage() {
        let message = "Hello from local";
        console.log("Inside function:", message);
    }

    showMessage();
    console.log("Outside function:", message);


    // Lab 3: Block Scope (var vs let vs const)

    if (true) {
        var x = 1;
        let y = 2;
        const z = 3;
    }

    console.log("var x:", x); // works

    // console.log(y); // error if uncommented
    // console.log(z); // error if uncommented


    // Lab 4: Closures

    function createCounter() {
        let count = 0;
        return function() {
            count++;
            return count;
        };
    }

    const counter1 = createCounter();
    const counter2 = createCounter();

    console.log("Counter1:", counter1());
    console.log("Counter1:", counter1());
    console.log("Counter2:", counter2());
    console.log("Counter2:", counter2());
</script>

</body>
</html>
