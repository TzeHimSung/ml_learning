var vm = new Vue({
    el: '#app',
    data: {
        isActive: true,
        haserror: false,
        activeColor: 'red',
        fontSize: 30
    },
    computed: {
        classObject: function () {
            return {
                active: this.isActive && !this.haserror,
                'text-danger': this.haserror && this.haserror.type === 'fatal'
            }
        }
    }
})