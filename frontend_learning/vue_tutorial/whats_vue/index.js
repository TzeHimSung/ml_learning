var app = new Vue({
    // 作用对象
    el: '#app_1',
    data: {
        message: 'Hello Vue! 您好，Vue!'
    }
})

// 利用v-bind实现动态绑定
var app2 = new Vue({
    el: '#app_2',
    data: {
        message: '页面加载于' + new Date().toLocaleString()
    }
})

// 利用v-if控制DOM对象是否可见
var app3 = new Vue({
    el: '#app_3',
    data: {
        seen: true
    }
})

// 利用v-for渲染列表
var app4 = new Vue({
    el: '#app_4',
    data: {
        todos: [
            { text: '学习JS' },
            { text: '学习Vue' },
            { text: '搞个牛逼东西' }
        ]
    }
})

// 利用v-on监听事件
var app5 = new Vue({
    el: '#app_5',
    data: {
        message: 'Hello Vue.js!'
    },
    methods: {
        reverseMessage: function () {
            this.message = this.message.split('').reverse().join('')
        }
    }
})

// 双向绑定
var app6 = new Vue({
    el: '#app_6',
    data: {
        message: 'Hello Vue!'
    }
})

// 定义一个vue组件
Vue.component('todo-item', {
    props: ['todo'],
    template: '<li>{{ todo.text }}</li>'
})

var app7 = new Vue({
    el: '#app_7',
    data: {
        groceryList: [
            { id: 0, text: 'vegetable' },
            { id: 1, text: 'apple' },
            { id: 2, text: 'banana' },
        ]
    }
})