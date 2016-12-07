/**
 * Created by zxc on 16/12/4.
 */
function search_hospital() {
    $.get('/paramedic/hospital/search?keyword=' + $("#keyword").val(), function(data, status, xhr) {
        if (xhr.status == 200) {
            if (data.length == 0) return;
            $(".noitem").remove();
            for (var i = 0; i < data.length; i++) {
                $('#itemslist').append(
                    "<li class='list-group-item noitem'>"
                    + "<span class='badge' onclick=enter_map(" + data[i].id + ")>map</span>" + data[i].name + "</li>"
                );
            }
        } else {
            console.log('problem');
        }
    }, dataType='json');
}

function enter_map(id) {
    window.location.href = '/paramedic/hospital/map?type=2&id=' + id;
}