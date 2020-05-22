$(document).ready(function(){
    var $listItems = $("#airlines");

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        listDatas = "";
        for( var i = 0; i < myArr.length; i++ ){
            listDatas += "<a href=\"airline.html?code=" + myArr[i].code  + "\"><li>" + myArr[i].name + "</li></a>";
        };
        $listItems.html(listDatas);
      }
    };
    xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec7d44718c8475bf16e4782", true);
    xmlhttp.send();
});
