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

function changeQuantityCart(obj, cartid, id){
    num = obj.value; //lấy ở product detail đưa ra số lượng bao nhiêu đểu mình mua
    if (!num) { //nếu không tồn tại num thì tức là lấy ở product ở phần home..show product
        num = 1;
    }
    strproductpriceid= "#productprice--" + cartid
    strcartcolorid = "#getCartColor--"+cartid
    strcartsizeid = "#getCartSize--"+cartid
    strcartgender = "#getCartgender--"+cartid
    strcartname = "#getCartName--"+cartid
    strcartprice = "#getCartPrice--"+cartid
    strcartimage = "#getImageCart--"+cartid;
    color = $(strcartcolorid).text()
    size = $(strcartsizeid).text()
    namecart = $(strcartname).text()
    gender = $(strcartgender).text()
    price = $(strcartprice).text()
    image = $(strcartimage).attr('src')
    $.ajax({
        type: 'POST',
        url: 'addcart/',
        data: { 'id':id,'name':namecart,'gender':gender, 'price':price,  'num': num,'color':color, 'size':size,'image':image, 'csrfmiddlewaretoken': csrftoken},
        dataType: "json",
        success: function (data) {
            $("#cartquantity").text(data.quantity);
            $("#totalquantity").text(data.quantity);
            $("#totalpricecart").text(data.totalprice);
            totalpricetax= parseInt(data.totalprice)+2000;
            $("#totalpricecarttax").text(totalpricetax);
            $(strproductpriceid).text(data.productprice);
        }
    });
}