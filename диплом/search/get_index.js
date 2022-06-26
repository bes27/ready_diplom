var json = lunr(function () {
    this.use(lunr.ru)
    this.ref('id')
    this.field('title')
    this.field('content')

    pages_data.forEach(function (doc) {
        this.add(doc)
    }, this)
}).toJSON()

$('#output').append('var index_json = ' + JSON.stringify(json))
console.log('var index_json = ' + JSON.stringify(json))
