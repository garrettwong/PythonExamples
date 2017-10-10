var btn = document.querySelector('#btnSubmit');
btn.addEventListener('click', function() {
    alert('click handler registered');

    var input = document.querySelector('input');

    console.log(input.value);

    //https://github.com/toddmotto/public-apis#animals
    //https://dog.ceo/dog-api/
    var dogApiUrl = 'https://dog.ceo/api/breeds/list/all';
    httpGetAsync(dogApiUrl, function(data) {
        alert('terrence!');
        console.log(data);
    })
});

// http request handlers
function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function httpPostAsync(url, data, callback) {
    var json_upload = "json_name=" + JSON.stringify(data);
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
        callback(xmlHttp.responseText);
    };
    xmlhttp.open("POST", url);
    xmlhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xmlhttp.send(json_upload);
}