





$(document).on('submit', '#createImageProduct', function (e) {
    e.preventDefault()
    $.ajax({
        type: "POST", //ở đây là dạng method GET hoặc POST
        url: "createimageproduct/",  //url 
        data: new FormData(this), //l điều này có thể truy cập đến file ex: img thay vì dùng serialize() ko thể truy cập đến file
        processData: false, // dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        contentType: false,// dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        dataType: 'html', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
        success: function (data, textStatus, jqXHR) {
            $('#createImageProductList').html(data)
            $("#createImageProduct")[0].reset()
            alert("Image was save in data")
        },
    });
})


$(document).on('submit', '#editImageProduct', function (e) {
    e.preventDefault()
    $.ajax({
        type: "POST", //ở đây là dạng method GET hoặc POST
        url: "editcreateimageproduct/",  //url 
        data: new FormData(this), //l điều này có thể truy cập đến file ex: img thay vì dùng serialize() ko thể truy cập đến file
        processData: false, // dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        contentType: false,// dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        dataType: 'html', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
        success: function (data, textStatus, jqXHR) {
            $('#createImageProductList').html(data)
            $("#editImageProduct")[0].reset()
            alert("Image was save in data")
        },
    });
})

