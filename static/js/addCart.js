
function getCookieCart(name) {
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
const csrftokenCart = getCookieCart('csrftoken');

    function addCart(id) {
        num = $("#number").val(); //lấy ở product detail đưa ra số lượng bao nhiêu để mình mua
        if (!num) { //nếu không tồn tại num thì tức là lấy ở product ở phần home..show product
            num = 1;
        }
        var getcolor = $('input[name="variantColor"]:checked').map(function(){
            return this.value;
        }).get()
        color=getcolor[0]
        var getsize = $('input[name="variantSize"]:checked').map(function(){
            return this.value;
        }).get()
        size=getsize[0]
        str = "#" + id;
        $.ajax({
            type: "POST", 
            url: 'addcart/',
            data: { 'id':id, 'num': num, 'color':color, 'size':size ,'csrfmiddlewaretoken': csrftokenCart},
            dataType: "json",
            success: function (data) {
                $("#cartquantity").text(data.quantity)
                // if (data.quantitproduct>=10){
                //     $(str).remove()
                // }
            }
        });
        // $.post("addcart/", {'id':id, 'num': num, 'csrfmiddlewaretoken': csrftoken},
        //     function (data) {
        //         $("#cartquantity").text(data.quantity)
        //     },
        // );
    }
 












