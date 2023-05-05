$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/menu/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="baby-pizza">
                                <a href="/menu/${ d.id }" class="font-weight-normal text-reset text-decoration-none">
                                    <div class="menu-image">
                                        <img src="/static/images/${d.image}" alt="${ d.description } " width="100%" />
                                    </div>
                                    <div class="menu-name">
                                        ${ d.name }
                                    </div>
                                </a>
                            </div>`
                });
                $('.pizza-menu').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});

$(document).ready(function() {
    $('.filter-btns').on('click', function(f) {
        f.preventDefault();
        let filterType = $(this).attr('id');
        $.ajax({
            url: '/menu/?pizza_filter=' + filterType,
            type: 'GET',
            success: function(resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="baby-pizza">
                                <a href="/menu/${ d.id }" class="font-weight-normal text-reset text-decoration-none">
                                    <div class="menu-image">
                                        <img src="/static/images/${d.image}" alt="${ d.description } " width="100%" />
                                    </div>
                                    <div class="menu-name">
                                        ${ d.name }
                                    </div>
                                </a>
                            </div>`
                });
                $('.pizza-menu').html(newHtml.join(''));
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});