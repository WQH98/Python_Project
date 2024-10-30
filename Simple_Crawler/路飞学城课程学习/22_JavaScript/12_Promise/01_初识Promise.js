/*
*   Promise 实例化的时候，传入的参数是一个函数，函数中接收两个参数：
*   传入的 resolve 和 reject 本身都是函数。其作用分别为：
*   resolve - 把 Promise 的状态从进行中变为成功状态。
*   reject - 把 Promise 的状态从进行中变为拒绝状态。
* */
var p = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('123');
    }, 5000);
}).then(res => {
    console.log(res)
})


/*
*   Promise的三种状态：
*   pending ：进行中，表示 Promise 还在执行阶段，没有执行完成。
*   fulfilled：成功状态，表示 Promise 成功执行完成。
*   rejected：拒绝状态，表示 Promise 执行被拒绝，也就是失败。
*   Promise 的状态，只可能是其中一种状态，从进行中变为成功或失败状态之后，状态就固定了，不会再发生改变。
* */

