Java.perform(function() {
    // 包、类
    var UpdateDialog = Java.use("com.azhon.appupdate.dialog.UpdateDialog");

    // Hook，替换
    UpdateDialog.show.implementation = function() {
        console.log("-----------------请求来了！！！-----------------");

        // 执行原来的方法
        // var ret = this.show();
        // return ret;
    }
})