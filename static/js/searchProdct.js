
$(function() {
    $('#id_name').keyup(function() {
        path = window.location.href+"searchproduct/"
        $.ajax({
            type: "GET",
            url: path,
            // url: "{% url 'appProduct:searchProduct' %}",
            data: {
                'search_text' : $('#id_name').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            dataType: 'html',
            success: function(data, textStatus, jqXHR){
                $('.undefined-number').text("searching....")
                $('#search_results').html(data)
            },
        })
    });
});

