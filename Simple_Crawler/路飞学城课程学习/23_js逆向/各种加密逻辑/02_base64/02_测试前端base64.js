window = global;

var s = "hello world";

var b = window.btoa(s);
console.log(b);
var a = window.atob(b);
console.log(a);

