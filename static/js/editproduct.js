

$(document).on('submit', '#editproduct', function(e){
    e.preventDefault()
    form =new FormData(this)
    var id = $(this).data('id')
    $.ajax({
        type: "POST", //ở đây là dạng method GET hoặc POST
        url: '/product/' + id + '/editproduct/',  //url 
        data: new FormData(this), //l điều này có thể truy cập đến file ex: img thay vì dùng serialize() ko thể truy cập đến file
        processData: false, // dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        contentType: false,// dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        dataType: 'json', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
        success: function (data) {
            alert("Edit success")
            $("#editproduct").html(data.html_form);
        }
    });
})


