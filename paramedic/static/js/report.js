/**
 * Created by zxc on 16/12/4.
 */
function send_report() {
    window.location.href = '/paramedic/home';
}
function back() {
    window.location.href = '/paramedic/home';
}
function sendImg(ele) {
    $("#loading").css("visibility", "visible");
    setTimeout("$('#loading').css('visibility', 'hidden')",3000);
}
