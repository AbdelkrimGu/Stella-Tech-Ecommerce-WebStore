$(document).on('keyup mouseup', ".primary-btn", function () {
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:' + productId + 'action:' + action)
    console.log('USER:', user)
    if (user == 'AnonymousUser') {
        alert('User is not authenticated')
    }
    else {
        addReview(productId, action);
    }
});