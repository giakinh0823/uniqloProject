$(document).on('click', '.deletecart', function() {
    var id = $(this).data('id')
    var action = confirm("Are you sure you want to delete this user?");
    if (action != false) {
        var childli = $(this).closest('li')
        $.ajax({
                url: '/basket/' + id + '/deletecart/',
                data: {
                    'id': id,
                },
                dataType: 'json',
                success: function(data) {
                    if (data.deleted) {
                        $("#cart-" + id).remove();
                    }
                    $('#totalquantity').text(data.quantity)
                    $('#listCartQuantity').text(data.listcart)
                    if (parseInt(data.quantity) > 0) {
                        $("#cartquantity").text(data.quantity);
                    } else {
                        $("#cartquantity").text('');
                        $("#disabledCartCheckout").attr("disabled", true);
                    }
                    $("#totalpricecart").text(data.totalprice);
                    totalpricetax = parseInt(data.totalprice) + 2000
                    $("#totalpricecarttax").text(totalpricetax)
                }
            })
            .done(function(data) { //sau khi Ajax nhận được data từ server trả về và user được save
                childli.hide() //ẩn đi li gần nhất
                $('.cart-size').text((parseInt($('.cart-size').text()) - 1)); //lấy giá trị text của thẻ button có class = product-size,  chuyển về dạng int rồi trừ đi 1, sau đó gán lại vào giá trị text của chính nó
            })
        return false;
    }
})