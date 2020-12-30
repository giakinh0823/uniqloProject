// const form = document.getElementById('createproduct') //lấy id của form createproduct
// form.addEventListener('submit', createproduct) //lắng nghe sự kiện , nếu sự kiện submit của form có id createproduct được thực hiện thì sẽ thực hiện hàm createproduct

// function createproduct(e){
//     e.preventDefault() //ngăn chặn hành động mặc định của việc gửi biểm mẫu(form)
//     $.ajax({
//         type: "POST", //ở đây là dạng method GET hoặc POST
//         url: "{% url 'appProduct:productuser' %}",  //url là bạn muốn rederict đến 
//         data: $("#createproduct").serialize(), //lấy hết dữ liệu ở trong biểu mẫu(form) này khi được gửi lên
//         dataType: 'json', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
//         success: function (response) {
//         }
//     });
// }

//ĐỊNH NGHĨA Ở PHÍA TRÊN. TÓM TẮT Ở PHÍA DƯỚI

// $(document).on('submit', '#createproduct', function(e){
//     e.preventDefault()
//     $.ajax({
//         type: "POST", //ở đây là dạng method GET hoặc POST
//         url: "/createproduct/",  //url 
//         data: $("#createproduct").serialize(), //lấy hết dữ liệu ở trong biểu mẫu(form) này khi được gửi lên
//         dataType: 'json', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
//         success: function (data) {
//             alert("create success")
//             $("#createproduct")[0].reset()
//         }
//     });
// })


$(document).on('submit', '#createproduct', function(e){
    e.preventDefault()
    $.ajax({
        type: "POST", //ở đây là dạng method GET hoặc POST
        url: "/createproduct/",  //url 
        data: new FormData(this), //l điều này có thể truy cập đến file ex: img thay vì dùng serialize() ko thể truy cập đến file
        processData: false, // dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        contentType: false,// dùng new FormData(this) phải có cái này ko sẽ bị lỗi
        dataType: 'json', //data mong đợi từ sever sẽ gửi về dưới dạng gì.ở đây thì theo dạng json
        success: function (data) {
            alert("create success")
            $("#createproduct")[0].reset()
        }
    });
})


