document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            alert(`Product ${productId} added to cart!`);
            // Add AJAX call to update cart here
        });
    });
});