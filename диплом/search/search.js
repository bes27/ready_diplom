var idx = lunr.Index.load(index_json)
var pages = pages_data.reduce(function (mem, page) {
    mem[page.id] = page
    return mem
}, {})

var queryString = window.location.search;
var urlParams = new URLSearchParams(queryString);
var query = urlParams.get("q")

if (query) {
    $('#search').val(query)
    var container = $('#results')
    var results = idx.search(query)
    console.log(results)
    results.forEach(function (res) {
        var page = pages[res.ref]

        container.append(`<div class="search_item">
            <a class="search_title" href="${page.link}">${page.title}</a><br/>
            <p class="search_description">${page.content.slice(0, 300)}...</p>
        </div>`);
    })

    if (results.length == 0) {
        $('#results').append('Ничего не найдено.');
    }
    // $('#yourDivName').append('yourtHTML');
} else {
    $('#results').append('Задана пустая строка.');
}
