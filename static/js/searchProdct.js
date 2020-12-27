

$(document).ready(function(){
   
    var search = $("#id_name"); //lấy text ở input
    var items  = $(".product__item");
 
    $("#searchButton").on("click", function(e){
         
        var v = search.val().toLowerCase(); 
        if(v == "") { 
            items.show();
            return;
        }
         $.each(items, function(){
             var it = $(this);
             var lb = it.find(".product__category-span").text().toLowerCase();
             if(lb.indexOf(v) == -1) 
                  it.hide();
         });
     });        
 });
