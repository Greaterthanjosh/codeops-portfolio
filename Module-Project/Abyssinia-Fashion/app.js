const PHONE = /^(?:09\d{8}|\+2519\d{8})$/;

const CART_STORAGE_KEY = "abyssiniaFashionCart";
const ORDER_STORAGE_KEY = "abyssiniaFashionLastOrder";

const state = {
  products: [],
  cart: [],
  search: "",
  category: "",
};

// DOM elements
const productsEl = document.querySelector("#products");
const searchEl = document.querySelector("#search");
const cartEl = document.querySelector("#cart-items");
const cartCountEl = document.querySelector("#cart-count");
const cartTotalEl = document.querySelector("#cart-total");
const categoryLinks = document.querySelectorAll("[data-category]");
const checkoutButton = document.querySelector("#checkout-button");

// Load products from JSON
async function loadProducts() {
  productsEl.textContent = "Loading products...";

  try {
    const response = await fetch("data/products.json");

    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }

    const products = await response.json();

    if (!Array.isArray(products)) {
      throw new Error("Product data is not an array.");
    }

    state.products = products;

    render();
  } catch (error) {
    productsEl.innerHTML = `
      <p>
        Could not load the products.
      </p>
    `;

    console.error("Product loading error:", error);
  }
}

// Render the application
function render() {
  renderProducts();
  renderCart();
}

// Render product cards
function renderProducts() {
  const term = state.search.trim().toLowerCase();

  const visibleProducts = state.products.filter(function (product) {
    const productName = String(product.name || "").toLowerCase();
    const productCategory = String(product.category || "");

    const matchesSearch = productName.includes(term);

    const matchesCategory =
      state.category === "" || productCategory === state.category;

    return matchesSearch && matchesCategory;
  });

  if (visibleProducts.length === 0) {
    productsEl.innerHTML = `
      <p>
        No products found.
      </p>
    `;

    return;
  }

  productsEl.innerHTML = visibleProducts
    .map(function (product) {
      const price = Number(product.price);

      return `
        <article
          class="product-card"
          data-id="${product.id}"
        >
          <img
            src="${product.image}"
            alt="${product.name}"
          >

          <div class="product-info">

            <h3 class="product-name">
              ${product.name}
            </h3>

            <p class="product-category">
              ${product.category}
            </p>

            <p class="product-price">
              ${
                Number.isFinite(price)
                  ? price.toLocaleString()
                  : "Price unavailable"
              } ETB
            </p>

            <button
              class="add-to-cart"
              type="button"
              data-id="${product.id}"
            >
              Add to Cart
            </button>

          </div>
        </article>
      `;
    })
    .join("");
}

// Render shopping cart
function renderCart() {
  if (state.cart.length === 0) {
    cartEl.innerHTML = `
      <li>Your cart is empty.</li>
    `;
  } else {
    cartEl.innerHTML = state.cart
      .map(function (item) {
        const price = Number(item.price) || 0;
        const quantity = Number(item.qty) || 0;

        return `
          <li data-id="${item.id}">

            <span>
              ${item.name}
            </span>

            <span>
              ${quantity} ×
              ${price.toLocaleString()} ETB
            </span>

            <button
              class="remove-from-cart"
              type="button"
            >
              Remove
            </button>

          </li>
        `;
      })
      .join("");
  }

  const itemCount = state.cart.reduce(function (sum, item) {
    return sum + (Number(item.qty) || 0);
  }, 0);

  cartCountEl.textContent = itemCount;

  cartTotalEl.textContent = cartTotal().toLocaleString() + " ETB";
}

// Calculate cart total
function cartTotal() {
  return state.cart.reduce(function (sum, item) {
    const price = Number(item.price);
    const quantity = Number(item.qty);

    if (!Number.isFinite(price) || !Number.isFinite(quantity)) {
      return sum;
    }

    return sum + price * quantity;
  }, 0);
}

// Save cart to localStorage
function save() {
  localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(state.cart));
}

// Load cart from localStorage
function load() {
  const savedCart = localStorage.getItem(CART_STORAGE_KEY);

  if (!savedCart) {
    return;
  }

  try {
    const parsedCart = JSON.parse(savedCart);

    if (!Array.isArray(parsedCart)) {
      state.cart = [];
      return;
    }

    state.cart = parsedCart.filter(function (item) {
      const quantity = Number(item.qty);

      return (
        item &&
        item.id !== undefined &&
        Number.isFinite(quantity) &&
        quantity > 0
      );
    });
  } catch (error) {
    state.cart = [];

    console.error("Could not restore the saved cart:", error);
  }
}

// Live search
searchEl.addEventListener("input", function (event) {
  state.search = event.target.value;

  renderProducts();
});

// Category filtering
categoryLinks.forEach(function (link) {
  link.addEventListener("click", function (event) {
    event.preventDefault();

    state.category = event.currentTarget.dataset.category;

    renderProducts();
  });
});

// Add to cart using event delegation
productsEl.addEventListener("click", function (event) {
  if (!event.target.matches(".add-to-cart")) {
    return;
  }

  const id = Number(event.target.dataset.id);

  const product = state.products.find(function (item) {
    return item.id === id;
  });

  if (!product) {
    return;
  }

  const price = Number(product.price);

  if (!Number.isFinite(price) || price < 0) {
    return;
  }

  const existingItem = state.cart.find(function (item) {
    return item.id === id;
  });

  if (existingItem) {
    existingItem.qty = (Number(existingItem.qty) || 0) + 1;
  } else {
    state.cart.push({
      ...product,
      price: price,
      qty: 1,
    });
  }

  save();
  render();
});

// Remove from cart using event delegation
cartEl.addEventListener("click", function (event) {
  if (!event.target.matches(".remove-from-cart")) {
    return;
  }

  const cartItem = event.target.closest("li");

  if (!cartItem) {
    return;
  }

  const id = Number(cartItem.dataset.id);

  state.cart = state.cart.filter(function (item) {
    return item.id !== id;
  });

  save();
  render();
});

// Create checkout form
function createCheckoutForm() {
  const existingCheckout = document.querySelector("#checkout-section");

  if (existingCheckout) {
    return existingCheckout;
  }

  const checkoutSection = document.createElement("section");

  checkoutSection.id = "checkout-section";

  checkoutSection.innerHTML = `
    <h2>Checkout</h2>

    <form id="checkout" novalidate>

      <label for="name">
        Name
      </label>

      <input
        id="name"
        name="name"
        type="text"
        autocomplete="name"
        required
      >


      <label for="phone">
        Phone (TeleBirr)
      </label>

      <input
        id="phone"
        name="phone"
        type="tel"
        placeholder="09xxxxxxxx"
        autocomplete="tel"
        required
      >


      <label for="area">
        Delivery area
      </label>

      <select
        id="area"
        name="area"
        required
      >
        <option value="">
          Select delivery area
        </option>

        <option value="Bole">
          Bole
        </option>

        <option value="Kazanchis">
          Kazanchis
        </option>

        <option value="Megenagna">
          Megenagna
        </option>
      </select>


      <p
        id="form-error"
        class="error"
        role="alert"
        aria-live="polite"
      ></p>


      <p id="checkout-total">
        Order Total:
        ${cartTotal().toLocaleString()} ETB
      </p>


      <button
        type="submit"
        id="place-order-button"
      >
        Place Order
      </button>


      <button
        type="button"
        id="cancel-checkout-button"
      >
        Cancel
      </button>

    </form>
  `;

  document.querySelector("main").appendChild(checkoutSection);

  return checkoutSection;
}

// Open checkout
function openCheckout() {
  if (state.cart.length === 0) {
    alert("Your cart is empty. Please add a product before checkout.");

    return;
  }

  const checkoutSection = createCheckoutForm();

  checkoutSection.style.display = "block";

  const checkoutTotal = document.querySelector("#checkout-total");

  checkoutTotal.textContent =
    "Order Total: " + cartTotal().toLocaleString() + " ETB";

  checkoutSection.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });

  document.querySelector("#name").focus();
}

// Validate checkout form
function validateCheckout(data) {
  // Check name
  if (!data.name.trim()) {
    return "Please enter your name.";
  }

  // Check phone
  if (!PHONE.test(data.phone.trim())) {
    return "Enter a valid Ethiopian phone.";
  }

  // Check delivery area
  if (!data.area) {
    return "Please select a delivery area.";
  }

  // Check cart
  if (state.cart.length === 0) {
    return "Your cart is empty.";
  }

  // Check cart items
  for (const item of state.cart) {
    const quantity = Number(item.qty);
    const price = Number(item.price);

    if (!Number.isFinite(quantity) || quantity <= 0) {
      return "Your cart contains an invalid quantity.";
    }

    if (!Number.isFinite(price) || price < 0) {
      return "Your cart contains an invalid product price.";
    }
  }

  return "";
}

// Place order
function placeOrder(data) {
  const order = {
    name: data.name.trim(),
    phone: data.phone.trim(),
    area: data.area,

    items: state.cart.map(function (item) {
      return {
        id: item.id,
        name: item.name,
        price: Number(item.price),
        qty: Number(item.qty),
      };
    }),

    total: cartTotal(),

    date: new Date().toISOString(),
  };

  // Save the order
  localStorage.setItem(ORDER_STORAGE_KEY, JSON.stringify(order));

  // Clear the cart
  state.cart = [];

  save();

  render();

  // Show confirmation
  showOrderConfirmation(order);
}

// Show validation error
function showCheckoutError(message) {
  const errorEl = document.querySelector("#form-error");

  if (!errorEl) {
    return;
  }

  errorEl.textContent = message;
}

// Show successful order confirmation
function showOrderConfirmation(order) {
  const checkoutSection = document.querySelector("#checkout-section");

  if (!checkoutSection) {
    return;
  }

  checkoutSection.innerHTML = `
    <div class="checkout-success">

      <h2>
        Order Confirmed!
      </h2>

      <p>
        Thank you,
        <strong>${order.name}</strong>.
      </p>

      <p>
        Your order will be delivered to
        <strong>${order.area}</strong>.
      </p>

      <p>
        TeleBirr phone:
        <strong>${order.phone}</strong>
      </p>

      <p>
        Order Total:
        <strong>
          ${order.total.toLocaleString()} ETB
        </strong>
      </p>

      <button
        type="button"
        id="continue-shopping-button"
      >
        Continue Shopping
      </button>

    </div>
  `;
}

// Handle checkout submission
document.addEventListener("submit", function (event) {
  if (!event.target.matches("#checkout")) {
    return;
  }

  event.preventDefault();

  const nameEl = document.querySelector("#name");

  const phoneEl = document.querySelector("#phone");

  const areaEl = document.querySelector("#area");

  const data = {
    name: nameEl.value,
    phone: phoneEl.value,
    area: areaEl.value,
  };

  // Get the first validation error
  const error = validateCheckout(data);

  showCheckoutError(error);

  // Stop if validation fails
  if (error) {
    if (!data.name.trim()) {
      nameEl.focus();
    } else if (!PHONE.test(data.phone.trim())) {
      phoneEl.focus();
    } else {
      areaEl.focus();
    }

    return;
  }

  // Place valid order
  placeOrder(data);
});

// Checkout button
checkoutButton.addEventListener("click", openCheckout);

// Cancel checkout / continue shopping
document.addEventListener("click", function (event) {
  if (event.target.matches("#cancel-checkout-button")) {
    const checkoutSection = document.querySelector("#checkout-section");

    if (checkoutSection) {
      checkoutSection.remove();
    }

    return;
  }

  if (event.target.matches("#continue-shopping-button")) {
    const checkoutSection = document.querySelector("#checkout-section");

    if (checkoutSection) {
      checkoutSection.remove();
    }

    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }
});

// Initialize the application
async function init() {
  load();

  await loadProducts();
}

init();
