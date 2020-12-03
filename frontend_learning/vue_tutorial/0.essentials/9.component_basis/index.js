Vue.component('button-counter', {
    data: function () {
        return {
            count: 0
        }
    },
    template: '<button v-on:click="count++">You clicked me {{count}} times.</button>'
})

Vue.component('blog-post', {
    props: ['post'],
    template: '\
    <div class="blog-post">\
        <h3>{{post.title}}</h3>\
        <button v-on:click="$emit(\'enlarge-text\', 1)">Enlarge text</button>\
        <div v-html="post.content"></div>\
    </div>\
    '
})

// var vm = new Vue({
//     el: '#app',
//     data: {
//         posts: [
//             { id: 1, title: 'title1' },
//             { id: 2, title: 'title2' },
//             { id: 3, title: 'title3' },
//         ]
//     }
// })

var vm2 = new Vue({
    el: '#blog-posts-events-demo',
    data: {
        posts: [
            { id: 1, content: 'hhhh' },
            { id: 2, content: 'hhhh' },
            { id: 3, content: 'hhhh' },
        ],
        postFontSize: 1
    }
})