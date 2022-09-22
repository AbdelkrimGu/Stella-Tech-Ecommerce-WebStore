$(document).on('keyup mouseup', ".update-cart", function () {
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:' + productId + 'action:' + action)
    console.log('USER:', user)
    if (user == 'AnonymousUser') {
        alert('User is not authenticated')
    }
    else {
        updateUserOrder(productId, action);
    }
});


$(document).on('keyup mouseup', ".update-wish", function () {
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:' + productId + 'action:' + action)

    console.log('USER:', user)
    if (user == 'AnonymousUser') {
        console.log('User is not authenticated')
    }
    else {
        updateUserWish(productId, action)
    }
})



function updateUserOrder(productId, action) {

    $.ajax({
        type: 'POST',
        url: '/update_item/',
        data: JSON.stringify({ 'productId': productId, 'action': action }),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        success: function (data) {

            $.post("/", { csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val() }, function (data) {
                $("#cart").replaceWith($(data).find("#cart"));
            });

            if (data.url) {
                window.location.href = data.url;
            }
            console.log("succeded");
        },
        error: function (data, textStatus, errorThrown) {
            alert('failed');
        }
    })

}

function updateUserWish(productId, action) {

    $.ajax({
        type: 'POST',
        url: '/update_wish/',
        data: JSON.stringify({ 'productId': productId, 'action': action }),
        csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),

        success: function (data) {
            $.post("/", { csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val() }, function (data) {
                $("#wish").replaceWith($(data).find("#wish"));
            });

            if (data.url) {
                window.location.href = data.url;
            }
            console.log("succeded");

        },

    })

}