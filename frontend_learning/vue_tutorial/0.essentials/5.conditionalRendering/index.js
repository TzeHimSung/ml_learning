var vm = new Vue({
    el: '#app',
    data: {
        flag: false,
        loginType: 'username',
        username: '',
        email: ''
    },
    methods: {
        sty: function () {
            if (this.loginType === 'username') {
                this.loginType = 'email'
            } else {
                this.loginType = 'username'
            }
        }
    }
})