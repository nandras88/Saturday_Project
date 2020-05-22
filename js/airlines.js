$(document).ready(function(){
    var $listItems = $("#airlines");

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        listDatas = "";
        for( var i = 0; i < myArr.length; i++ ){
            listDatas += "<a href=\""+ myArr[i].url +"\"><li>" + myArr[i].name + "</li></a>";
        };
        $listItems.html(listDatas);
      }
    };
    xmlhttp.open("GET", "https://api.jsonbin.io/b/5ec7a5c8bbaf1f258944d748/1", true);
    xmlhttp.send();
});
