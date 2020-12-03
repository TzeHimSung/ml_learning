var vm = new Vue({
    el: '#app',
    data: {
        message: '',
        message2: '',
        checked: false,
        checkedNames: [],
        picked: [],
        selected: []
    }
})

var vm2 = new Vue({
    el: '#app2',
    data: {
        selected: []
    }
})

var vm3 = new Vue({
    el: '#app3',
    data: {
        selected: '',
        options: [
            { text: 'One', value: 'A' },
            { text: 'Two', value: 'B' },
            { text: 'Three', value: 'C' }
        ]
    }
})

var vm4 = new Vue({
    el: '#app4',
    data: {
        picked: '',
        toggle: false,
        selected: ''
    }
})

var vm5 = new Vue({
    el: '#app5',
    data: {
        pick: '',
        a: 'a'
    }
})