$(document).on('click', '.deletefavourite', function() { 
    var id = $(this).data('id') 
    var action = confirm("Are you sure you want to delete this user?");
    if (action != false) {
        var childTr = $(this).closest('tr')
        $.ajax({
            url: '/favourite/' + id + '/deletefavourite/',
            data: {
                'id': id,
            },
            dataType: 'json',
            success: function (data) {
                if (data.deleted) {
                    $("#favourite-" + id).remove();
                }
                if(data.quantityfavourite>0){
                    $("#favouritequantity").text(data.quantityfavourite)
                }else{
                    $("#favouritequantity").text('')
                }
            }
        })
        .done(function(data) {    //sau khi Ajax nhận được data từ server trả về và user được save
            childTr.hide()     //ẩn đi li gần nhất
            $('.favourite-size').text((parseInt($('.favourite-size').text()) - 1));  //lấy giá trị text của thẻ button có class = product-size,  chuyển về dạng int rồi trừ đi 1, sau đó gán lại vào giá trị text của chính nó
        })
        return false;
    }
})