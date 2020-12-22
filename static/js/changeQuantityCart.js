function getCookie(name) {
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
const csrftoken = getCookie('csrftoken');

function changeQuantityCart(obj, id){
    num = obj.value; //lấy ở product detail đưa ra số lượng bao nhiêu đểu mình mua
    if (!num) { //nếu không tồn tại num thì tức là lấy ở product ở phần home..show product
        num = 1;
    }
    $.ajax({
        type: 'POST',
        url: 'addcart/',
        data: { 'id':id, 'num': num, 'csrfmiddlewaretoken': csrftoken},
        dataType: "json",
        success: function (data) {
            $("#cartquantity").text(data.quantity)
        }
    });
}