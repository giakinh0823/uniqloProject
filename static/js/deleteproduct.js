

$(document).on('click', '.delete', function() { 
    var id = $(this).data('id') 
    var action = confirm("Are you sure you want to delete this user?");
    if (action != false) {
        var childLi = $(this).closest('li')
        $.ajax({
            url: '/product/' + id + '/deleteproduct/',
            data: {
                'id': id,
            },
            dataType: 'json',
            success: function (data) {
                if (data.deleted) {
                    $("#product-" + id).remove();
                }
            }
        })
        .done(function(data) {    //sau khi Ajax nhận được data từ server trả về và user được save
            childLi.hide()
            $('.product-size').text((parseInt($('.product-size').text()) - 1));  //lấy giá trị text của thẻ span có class = product-size,  chuyển về dạng int rồi trừ đi 1, sau đó gán lại vào giá trị text của chính nó
        })
        return false;
    }
})