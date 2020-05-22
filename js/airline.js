$(document).ready(function(){

    function getUrlVars() {
        var vars = {};
        var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
            vars[key] = value;
        });
        return vars;
    };
    
    function getUrlParam(parameter, defaultvalue){
        var urlparameter = defaultvalue;
        if(window.location.href.indexOf(parameter) > -1){
            urlparameter = getUrlVars()[parameter];
            }
        return urlparameter;
    };
    
    
    var code = getUrlParam('code','Empty');
    
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        listDatas = "";
        for( var i = 0; i < myArr.length; i++ ){
            if( myArr[i].code == code )
            {
                console.log(myArr[i].code);
                console.log(myArr[i].name);
                console.log(myArr[i].flights);
                console.log(myArr[i].airNum);
                console.log(myArr[i].delAvg);
                console.log(myArr[i].minAvg);
                console.log(myArr[i].topPort);

            }
            // listDatas += "<a href=\"airline.html?code=" + myArr[i].code  + "\"><li>" + myArr[i].name + "</li></a>";
        };
        //$listItems.html(listDatas);
      }
    };
    xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec7d44718c8475bf16e4782", true);
    xmlhttp.send();

});

