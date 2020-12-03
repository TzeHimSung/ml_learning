var vm = new Vue({
    el: '#app',
    data: {
        pm: 'Parent',
        items: [
            { message: 'Foo', isp: true },
            { message: 'Bar', isp: false }
        ],
        detail: {
            title: 'More detail of this repo:',
            author: 'JHSeng',
            date: '07/20/2020'
        },
        numbers: [1, 2, 3, 4, 5],
        sets: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    },
    computed: {
        evenNumbers: function () {
            return this.numbers.filter((item) => {
                return item % 2 === 0
            })
        }
    },
    methods: {
        even: function (numbers) {
            return numbers.filter((number) => {
                return number % 2 === 0
            })
        }
    }
})

Vue.component('todo-item', {
    template: '\
    <li>\
        {{title}}\
        <button v-on:click="$emit(\'remove\')">Remove</button>\
    </li>\
    ',
    props: ['title']
})

new Vue({
    el: '#todo-list-example',
    data: {
        newTodoText: '',
        todos: [
            { id: 1, title: 'Do the dishes' },
            { id: 2, title: 'Take out the trash' },
            { id: 3, title: 'Mow the lawn' },
        ],
        nextTodoId: 4
    },
    methods: {
        addNewTodo: function () {
            this.todos.push({
                id: this.nextTodoId++,
                title: this.newTodoText
            })
            this.newTodoText = ''
        }
    }
})