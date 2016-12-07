/**
 * Created by zxc on 16/12/4.
 */
function getUrlArgObject(){
    // 获取URL中?之后的字符
    var str = location.search;
    str = str.substring(1,str.length);

    var arr = str.split("&");
    var obj = new Object();

    for(var i = 0; i < arr.length; i++) {
        var tmp_arr = arr[i].split("=");
        obj[decodeURIComponent(tmp_arr[0])] = decodeURIComponent(tmp_arr[1]);
    }
    return obj;
}

function getTargetLocation() {
    var args = getUrlArgObject();
    var type = args['type'];
    var id = args['id'];
    var image = '/static/images/beachflag.png';

    if (type == 1) {
        //get patients location
        $.get('/paramedic/patient/location', function(data, status, xhr) {
            if (xhr.status == 200) {
                for (var i = 0; i < data.length; i++) {
                    var pt = {lat: data[i].lat, lng: data[i].lon};
                    var marker = new google.maps.Marker({
                        position: pt,
                        map: map,
                        title: '',
                        icon:image
                    });
                }
            } else {
                console.log('network pr');
            }
        }, dataType='json');
    } else if (type == 2) {
        //get hospital location
        $.get('/paramedic/hospital/location?id='+ id, function(data, status, xhr) {
            if (xhr.status == 200) {
                var pt = {lat: data.lat, lng: data.lon};
                var marker = new google.maps.Marker({
                    position: pt,
                    map: map,
                    title: data.name,
                    icon:image
                });
            } else {
                console.log('network pr');
            }
        }, dataType='json');
    }
}

function NavigationTool() {
   var mode = google.maps.DirectionsTravelMode.DRIVING; //谷歌地图路线指引的模式
   var directionsDisplay = new google.maps.DirectionsRenderer();   //地图路线显示对象
   var directionsService = new google.maps.DirectionsService();    //地图路线服务对象
   var directionsVisible = true;  //是否显示路线
   directionsDisplay.setMap(null);
   directionsDisplay.setMap(map);
   var Navigpoints = []; //起终点
   google.maps.event.addListener(map, "click", function(evt) {
       if (Navigpoints.length == 0) {
           if (confirm("Use current point as start？")) {
               Navigpoints.push(evt.latLng);
           }
       } else {
           if (Navigpoints.length >= 2) { points = []; google.maps.event.clearListeners(map, "click"); return; }
           if (confirm("Use current point as end？")) {
               Navigpoints.push(evt.latLng);
               var request = {
                   origin: Navigpoints[0], //起点
                   destination: Navigpoints[1], //终点
                   travelMode: mode,
                   optimizeWaypoints: true,
                   avoidHighways: false,
                   avoidTolls: false
               };
               directionsService.route(
                request,
                function(response, status) {
                    if (status == google.maps.DirectionsStatus.OK) {
                        directionsDisplay.setDirections(response);
                        //定时清除线路
                        setTimeout(function() { directionsDisplay.setMap(null) }, 80000);
                    }
                }
            );
           }
       }

   });
   directionsVisible = true;
}




