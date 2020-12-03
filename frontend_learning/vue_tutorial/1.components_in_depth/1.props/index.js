Vue.component('blog-post', {
    props: ['postTitle'],
    template: '<h3>{{postTitle}}</h3>'
})

var Comp = {
    props: {
        num1: Number,
        num2: Number,
        des: String
    },
    template: '<span>{{des}}: {{num1+num2}}</span>'
}

var BoolTest = {
    props: {
        flag: Boolean
    },
    template: '<span>{{flag}}</span>'
}

var GetAllProps = {
    props: {
        id: Number,
        title: String
    },
    template: '<p>{{title}} with number: {{id}}</p>'
}

Vue.component('base-input', {
    inheritAttrs: false,
    props: ['label', 'value'],
    template: '\
        <label>\
            {{label}}\
            <input\
                v-bind="$attrs"\
                v-bind:value="value"\
                v-on:input="$emit(\'input\', $event.target.value)"\
            >\
        </label>\
    '
})

var vm = new Vue({
    el: '#app',
    components: {
        'comp': Comp,
        'bool-test': BoolTest,
        'getallp': GetAllProps
    },
    data: {
        obj: {
            id: 1,
            title: 'this is a title'
        }
    },
    methods: {
        addone: function () {
            this.obj.id += 1
        },
        clear: function () {
            this.obj.id = 0
        }
    }
})