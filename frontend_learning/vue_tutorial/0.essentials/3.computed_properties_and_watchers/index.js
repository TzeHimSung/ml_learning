var vm = new Vue({
    el: '#example',
    data: {
        message: 'Hello'
    },
    computed: {
        reversedMessage: {
            // 计算属性默认只有getter
            get: function () {
                return this.message.split('').reverse().join('')
            },
            // 你也可以自己写个setter
            set: function (newVal) {
                this.message = newVal.split('').reverse().join('')
            }
        }
    },
    methods: {
        btnc: function () {
            alert('before: ' + this.message)
            alert('after: ' + this.reversedMessage)
            this.message = this.reversedMessage
        }
    }
})

var vm2 = new Vue({
    el: '#watch-example',
    data: {
        question: '',
        answer: 'I cannot give you answer until you ask a question.'
    },
    watch: {
        question: function (newVal, oldVal) {
            this.answer = 'Waiting for you to stop typing...'
            this.debouncedGetAnswer()
        }
    },
    created: function () {
        this.debouncedGetAnswer = _.debounce(this.getAnswer, 500)
    },
    methods: {
        getAnswer: function () {
            if (this.question.indexOf('?') === -1) {
                this.answer = 'Question should contain a "?" mark'
                return
            }
            this.answer = 'Thinking...'
            axios.get('https://yesno.wtf/api')
                .then(function (res) {
                    this.answer = _.capitalize(res.data.answer)
                })
                .catch(function (error) {
                    this.answer = 'Error! Could not reach the API...' + error
                })
        }
    }
})