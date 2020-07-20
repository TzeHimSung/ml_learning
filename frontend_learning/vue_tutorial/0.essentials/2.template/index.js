var vm = new Vue({
    el: "#app",
    data: {
        msg: 'test msg',
        rawhtml: '<span style="color:red">This should be red</span>',
        isbuttondisabled: false,
        seen: false,
        url: 'https://www.google.com'
    },
    methods: {
        btnclick: function () {
            console.log(this.url)
        }
    }
})