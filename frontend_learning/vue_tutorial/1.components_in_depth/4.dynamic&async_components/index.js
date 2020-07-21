Vue.component('async-example', function (resolve, reject) {
    setTimeout(function () {
        // 向resolve回调传递组件定义
        resolve({
            template: '<div>I am async!</div>'
        })
    }, 1000)
})

Vue.component('async-webpack-example', function (resolve) {
    // 这个特殊的require语法将会告诉webpack
    // 自动将你的构建代码切割成多个包, 这些包会通过ajax请求加载
    require(['./my-async-component'], resolve)
})

Vue.component('async-webpack-example', () => import('./my-async-component'))