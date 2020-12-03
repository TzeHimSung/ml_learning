// var data = {
//     a: 1
// }

// var vm = new Vue({
//     data: data
// })

// console.log(vm.a == data.a)

// vm.a = 2
// console.log('data.a is: ' + data.a)

// data.a = 3
// console.log('vm.a is: ' + vm.a)

// var obj = {
//     foo: 'bar'
// }

// Object.freeze(obj)

// new Vue({
//     el: '#app',
//     data: obj
// })

var data = {
    a: 1
}

var vm = new Vue({
    el: '#example',
    data: data,
    created: function () {
        // this 指向vm
        console.log('a is: ' + this.a)
    },
    watch: {
        a: function (newVal, oldVal) {
            console.log('new val is: ' + newVal)
            console.log('old val is: ' + oldVal)
        }
    }
})

// console.log(vm.$data === data)
// console.log(vm.$el === document.getElementById('example'))