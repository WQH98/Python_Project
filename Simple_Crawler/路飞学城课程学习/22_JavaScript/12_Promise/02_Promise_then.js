/*
*   执行 resolve 时，Promise 状态变为 fulfilled
*   会执行 .then 方法。then 方法接收的参数也是一个函数
*   函数中携带一个参数，该参数是 resolve(res) 返回的数据。
* */

var p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('哎呦喂');
    }, 5000);
}).then(res => {
    console.log(res);
})
