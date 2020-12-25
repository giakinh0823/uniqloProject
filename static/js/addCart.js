
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
    $.ajax({
        type: "POST", 
        url: 'addcart/',
        data: { 'id':id, 'num': num, 'csrfmiddlewaretoken': csrftokenCart},
        dataType: "json",
        success: function (data) {
            $("#cartquantity").text(data.quantity)
        }
    });
    // $.post("addcart/", {'id':id, 'num': num, 'csrfmiddlewaretoken': csrftoken},
    //     function (data) {
    //         $("#cartquantity").text(data.quantity)
    //     },
    // );
}












