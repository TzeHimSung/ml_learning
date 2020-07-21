// 组件的全局注册
// 一旦声明，任何地方的Vue对象都可以用
Vue.component('component-1', {
    data: function () {
        return {
            msg1: 'this is the first component'
        }
    },
    template: '<p>{{msg1}}</p>'
})

// 组件的局部注册
// 与全局注册相比，没有名字，且需要在Vue对象里引入
var Component2 = {
    data: function () {
        return {
            msg2: 'this is the second one'
        }
    },
    template: '<p>{{msg2}}</p>'
}

var vm = new Vue({
    el: '#app',
    components: {
        'component-2': Component2
    },
    data: {
    }
})