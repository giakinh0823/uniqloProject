
$(function() {
    $('#id_name').keyup(function() {
        $.ajax({
            type: "GET",
            url: "searchproduct/",
            data: {
                'search_text' : $('#id_name').val(),
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
        });
    });
});

function searchSuccess(data, textStatus, jqXHR)
{
    $('#search_results').html(data)
}
