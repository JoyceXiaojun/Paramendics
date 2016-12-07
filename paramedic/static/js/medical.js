/**
 * Created by zxc on 16/12/4.
 */
function search(type) {
    $.get('/paramedic/medical/search?name=' + $("#pname").val() + '&type=' + type, function(data, status, xhr) {
        if (xhr.status == 200) {
            if (data.length == 0) return;
            $(".noitem").remove();
            for (var i = 0; i < data.length; i++) {
                $('#itemslist').append(
                    "<li class='list-group-item noitem' onclick='enter(" + data[i].id + ")'>" + data[i].name + "</li>"
                );
            }
        } else {
            console.log('problem');
        }
    }, dataType='json');
}

function enter(id) {
    window.location.href='http://localhost:8000/paramedic/medical/' + id;
}