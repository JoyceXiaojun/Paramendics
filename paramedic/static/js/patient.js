/**
 * Created by zxc on 16/12/4.
 */
var availableTags = [
  "Paul Smith"
];
$( "#pname" ).autocomplete({
  source: availableTags
});
function search() {
    $.get('/paramedic/patient/search?name=' + $("#pname").val(), function(data, status, xhr) {
        if (xhr.status == 200) {
            if (data.length == 0) return;
            $(".nopatient").remove();
            for (var i = 0; i < data.length; i++) {
                $('#patientlist').append(
                    "<li class='list-group-item nopatient' onclick='enter(" + data[i].pid + ")'>" + data[i].name + "</li>"
                );
            }
        } else {
            console.log('problem');
        }
    }, dataType='json');
}

function enter(id) {
    window.location.href='/paramedic/patient/' + id;
}

function sendImg(ele) {
    $("#loading").css("display", "block");
    setTimeout("$('#loading').css('display', 'none')",3000);
}
