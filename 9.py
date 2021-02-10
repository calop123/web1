#!C:\Users\chosun\AppData\Local\Programs\Python\Python37-32\python.exe
print("content-type: text/html; charset=utf-8\n")

print('''

<!DOCTYPE html>
<html>
<head>
<script>
    function loadDemo() {
        if (navigator.geolocation) {
            alert("Your browser supports geolocation service.");
            getloc();
        } else {
            alert("Your browser doesn't support geolocation service.");
        }
    }
    function getloc() {
        //navigator.geolocation.getCurrentPosition(updateLocation, handleLocationError);
        navigator.geolocation.watchPosition(updateLocation, handleLocationError, {maximumAge:2000});
    }
    function updateLocation(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        var accuracy = position.coords.accuracy;
        document.getElementById("latitude").innerHTML = latitude;
        document.getElementById("longitude").innerHTML = longitude;
        document.getElementById("accuracy").innerHTML = accuracy;
    }
    function handleLocationError(error) {
        switch(error.code) {
        case error.UNKNOWN_ERROR:
            alert("unknown error");
            break;
        case error.PERMISSION_DENIED:
            alert("Permission to use Geolocation was denied");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("unavailable");
            break;
        case error.TIMEOUT:
            alert("timeout error");
            break;
        }
    }
</script>
</head>
<body onload="loadDemo()">
<h1 id="latitude">?</h1>
<h1 id="longitude">?</h1>
<h1 id="accuracy">?</h1>
</body>
</html>


''')
