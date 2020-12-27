
$(function() {
    $('#id_name').keyup(function() {
        $.ajax({
            type: "GET",
            url: "searchproduct/",
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

