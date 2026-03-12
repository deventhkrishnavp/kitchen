// Shopping Cart Logic for R Vaibhava Cafe

// Initialize cart from localStorage
let cart = JSON.parse(localStorage.getItem('cafeCart')) || [];

// Function to add item to cart
function addToCart(name, price) {
    const existingItem = cart.find(item => item.name === name);
    
    if (existingItem) {
        existingItem.quantity += 1;
    } else {
        cart.push({
            name: name,
            price: parseFloat(price),
            quantity: 1
        });
    }
    
    saveCart();
    showToast(`${name} added to order!`);
    updateCartUI();
}

// Function to save cart to localStorage
function saveCart() {
    localStorage.setItem('cafeCart', JSON.stringify(cart));
}

// Function to get total price
function getCartTotal() {
    return cart.reduce((total, item) => total + (item.price * item.quantity), 0);
}

// Simple toast notification
function showToast(message) {
    const toast = document.createElement('div');
    toast.className = 'fixed bottom-10 right-10 bg-brand-black text-white px-6 py-3 rounded-xl shadow-2xl z-[100] animate__animated animate__fadeInUp border border-brand-red';
    toast.innerHTML = `<div class="flex items-center gap-3"><i class="fas fa-check-circle text-brand-red"></i> ${message}</div>`;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.replace('animate__fadeInUp', 'animate__fadeOutDown');
        setTimeout(() => toast.remove(), 1000);
    }, 3000);
}

// Function to update global cart counts or UI elements if needed
function updateCartUI() {
    // This can be expanded to update a cart counter in the nav
    console.log('Cart updated:', cart);
    
    // Dispatch custom event for pages like order.html to listen to
    window.dispatchEvent(new CustomEvent('cartUpdated', { detail: cart }));
}

// Initialize UI
document.addEventListener('DOMContentLoaded', () => {
    updateCartUI();
});
