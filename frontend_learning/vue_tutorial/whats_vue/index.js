var app = new Vue({
    // 作用对象？
    el: '#app_1',
    data: {
        message: 'Hello Vue! 您好，Vue!'
    }
})

var app2 = new Vue({
    el: '#app_2',
    data: {
        message: '页面加载于' + new Date().toLocaleString()
    }
})

var app3 = new Vue({
    el: '#app_3',
    data: {
        seen: true
    }
})

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

var app6 = new Vue({
    el: '#app_6',
    data: {
        message: 'Hello Vue!'
    }
})

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