
function getCookieFavourite(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftokenFavourite = getCookieFavourite('csrftoken');

function addFavourite(id) {
    strblack = "#favourite--icon--black--"+id;
    strred = "#favourite--icon--red--" + id;
    strcheckbox = "checkbox--"+ id;
    $.ajax({
        type: "POST",
        url: 'addfavourite/',
        data: { 'id': id, 'csrfmiddlewaretoken': csrftokenFavourite },
        dataType: "json",
        success: function (data) {
            if(data.quantityfavourite>0){
                $("#favouritequantity").text(data.quantityfavourite)
            }
            if(data.quantityfavourite<=0){
                $("#favouritequantity").text('')
            }
            if(data.check==1){
                $(strblack).css({'opacity':'0'})
                $(strred).css({'fill':'red', 'opacity':'1'})
            }else{
                $(strred).css({'opacity':'0'})
                $(strblack).css({'fill':'black', 'opacity':'1'})
            }
            
        }
    });
}



