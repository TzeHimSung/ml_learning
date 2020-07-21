Vue.component('base-checkbox', {
    model: {
        prop: 'checked',
        event: 'change'
    },
    props: {
        checked: Boolean
    },
    template: '\
        <input\
            type="checkbox"\
            v-bind:checked="checked"\
            v-on:change="$emit(\'change\', $event.target.checked)"\
        >\
    '
})

Vue.component('base-input', {
    inheritAttrs: false,
    props: ['label', 'value'],
    computed: {
        inputListeners: function () {
            var vm = this
            return Object.assign({}, this.$listeners, {
                input: function (event) {
                    vm.$emit('input', event.target.value)
                }
            })
        }
    },
    template: '\
        <label>\
            {{label}}\
            <input\
                v-bind="$attrs"\
                v-bind:value="value"\
                v-on="inputListeners"\
            >\
        </label>\
    '
})

var vm = new Vue({
    el: '#app',
    data: {
        cb: false
    }
})