var Comp1 = {
    data: function () {
        return {
            a: 1
        }
    },
    template: '\
        <div>\
            <button @click="clicked">get father comp</button>\
            <br>\
            <input ref="inp">\
        </div>\
    ',
    methods: {
        clicked: function () {
            // 访问根实例数据
            // alert(this.$root.b)
            // 访问父实例数据
            alert(this.$parent.b)
            this.$parent.f()
        }
    }
}

var vm = new Vue({
    el: '#app',
    components: {
        'comp1': Comp1
    },
    data: {
        b: 2
    },
    methods: {
        f: function () {
            alert('this is parent function')
        },
        cli: function () {
            // debugger
            alert(this.$refs.refcomp1.a)
            this.$refs.refcomp1.$refs.inp.focus()
        }
    }
})