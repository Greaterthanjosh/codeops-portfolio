// Regular expression for validating Ethiopian phone numbers.
// Accepts: 09xxxxxxxx or +2519xxxxxxxx
const PHONE = /^(?:09\d{8}|\+2519\d{8})$/;

// Keys used to save and retrieve data from localStorage.
const CART_STORAGE_KEY = "abyssiniaFashionCart";
const ORDER_STORAGE_KEY = "abyssiniaFashionLastOrder";

// Central state object: stores the current application data.
const state = {
  products: [],
  cart: [],
  search: "",
  category: "",
};

// DOM elements: connect JavaScript to HTML elements.
const productsEl = document.querySelector("#products");
const searchEl = document.querySelector("#search");
const cartEl = document.querySelector("#cart-items");
const cartCountEl = document.querySelector("#cart-count");
const cartTotalEl = document.querySelector("#cart-total");
const categoryLinks = document.querySelectorAll("[data-category]");
const checkoutButton = document.querySelector("#checkout-button");

// Load products from the JSON file.
async function loadProducts() {
  productsEl.textContent = "Loading products...";

  try {
    // fetch() gets the product data from the JSON file.
    const response = await fetch("data/products.json");

    // Check whether the request was successful.
    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }

    // Convert the JSON response into JavaScript data.
    const products = await response.json();

    // Make sure the returned data is an array.
    if (!Array.isArray(products)) {
      throw new Error("Product data is not an array.");
    }

    // Store the products in our application state.
    state.products = products;

    // Update the page.
    render();
  } catch (error) {
    // Display an error if loading fails.
    productsEl.innerHTML = `
      <p>
        Could not load the products.
      </p>
    `;

    // Show the technical error in the browser console.
    console.error("Product loading error:", error);
  }
}

// Main render function.
// Calls the functions responsible for displaying products and cart.
function render() {
  renderProducts();
  renderCart();
}

// Render the product cards.
function renderProducts() {
  // Get the search text, remove extra spaces, and convert to lowercase.
  const term = state.search.trim().toLowerCase();

  // filter() creates a new array containing matching products.
  const visibleProducts = state.products.filter(function (product) {
    // Convert values to strings and lowercase them for searching.
    const productName = String(product.name || "").toLowerCase();
    const productCategory = String(product.category || "");

    // Check whether the product name matches the search.
    const matchesSearch = productName.includes(term);

    // Check whether the product matches the selected category.
    // An empty category means all categories are allowed.
    const matchesCategory =
      state.category === "" || productCategory === state.category;

    // Product must satisfy both conditions.
    return matchesSearch && matchesCategory;
  });

  // If there are no matching products, display a message.
  if (visibleProducts.length === 0) {
    productsEl.innerHTML = `
      <p>
        No products found.
      </p>
    `;

    // Stop the function here.
    return;
  }

  // map() converts each product object into an HTML product card.
  productsEl.innerHTML = visibleProducts
    .map(function (product) {
      // Convert the product price into a number.
      const price = Number(product.price);

      // Template literal: creates dynamic HTML.
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
                // Display a formatted price if it is a valid number.
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
    // Join all generated product cards into one HTML string.
    .join("");
}

// Render the shopping cart.
function renderCart() {
  // Check whether the cart is empty.
  if (state.cart.length === 0) {
    cartEl.innerHTML = `
      <li>Your cart is empty.</li>
    `;
  } else {
    // map() creates HTML for every cart item.
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

  // reduce() calculates the total number of products in the cart.
  const itemCount = state.cart.reduce(function (sum, item) {
    return sum + (Number(item.qty) || 0);
  }, 0);

  // Update the cart count in the HTML.
  cartCountEl.textContent = itemCount;

  // Calculate and display the cart total.
  cartTotalEl.textContent = cartTotal().toLocaleString() + " ETB";
}

// Calculate the total price of everything in the cart.
function cartTotal() {
  // reduce() adds price × quantity for every cart item.
  return state.cart.reduce(function (sum, item) {
    const price = Number(item.price);
    const quantity = Number(item.qty);

    // Ignore invalid price or quantity values.
    if (!Number.isFinite(price) || !Number.isFinite(quantity)) {
      return sum;
    }

    return sum + price * quantity;
  }, 0);
}

// Save the cart to localStorage.
function save() {
  // JSON.stringify converts the JavaScript array into a string.
  localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(state.cart));
}

// Load the saved cart from localStorage.
function load() {
  const savedCart = localStorage.getItem(CART_STORAGE_KEY);

  // If nothing was saved, stop here.
  if (!savedCart) {
    return;
  }

  try {
    // JSON.parse converts the stored string back into JavaScript data.
    const parsedCart = JSON.parse(savedCart);

    // Make sure the saved data is an array.
    if (!Array.isArray(parsedCart)) {
      state.cart = [];
      return;
    }

    // Keep only cart items with valid quantities.
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
    // If saved data is corrupted, start with an empty cart.
    state.cart = [];

    console.error("Could not restore the saved cart:", error);
  }
}

// Live search: runs whenever the user types.
searchEl.addEventListener("input", function (event) {
  // Store the current search text in state.
  state.search = event.target.value;

  // Re-render products using the new search value.
  renderProducts();
});

// Category filtering.
categoryLinks.forEach(function (link) {
  // Add a click event listener to every category link.
  link.addEventListener("click", function (event) {
    // Prevent the "#" link from reloading/changing the page.
    event.preventDefault();

    // Read the category from the data-category attribute.
    state.category = event.currentTarget.dataset.category;

    // Re-render products using the selected category.
    renderProducts();
  });
});

// Add to cart using event delegation.
productsEl.addEventListener("click", function (event) {
  // Ignore clicks that are not Add to Cart buttons.
  if (!event.target.matches(".add-to-cart")) {
    return;
  }

  // Get the product ID from the button.
  const id = Number(event.target.dataset.id);

  // find() searches for the product with this ID.
  const product = state.products.find(function (item) {
    return item.id === id;
  });

  // Stop if the product cannot be found.
  if (!product) {
    return;
  }

  // Convert the price to a number.
  const price = Number(product.price);

  // Reject invalid or negative prices.
  if (!Number.isFinite(price) || price < 0) {
    return;
  }

  // Check whether this product is already in the cart.
  const existingItem = state.cart.find(function (item) {
    return item.id === id;
  });

  if (existingItem) {
    // If it already exists, increase its quantity.
    existingItem.qty = (Number(existingItem.qty) || 0) + 1;
  } else {
    // Otherwise add a new item to the cart.
    state.cart.push({
      // Spread syntax copies the product properties.
      ...product,
      price: price,
      qty: 1,
    });
  }

  // Save the updated cart.
  save();

  // Re-render the page.
  render();
});

// Remove from cart using event delegation.
cartEl.addEventListener("click", function (event) {
  // Ignore clicks that are not Remove buttons.
  if (!event.target.matches(".remove-from-cart")) {
    return;
  }

  // Find the cart item containing the clicked button.
  const cartItem = event.target.closest("li");

  if (!cartItem) {
    return;
  }

  // Get the product ID from the cart item.
  const id = Number(cartItem.dataset.id);

  // filter() creates a new cart without the selected item.
  state.cart = state.cart.filter(function (item) {
    return item.id !== id;
  });

  // Save and re-render the updated cart.
  save();
  render();
});

// Create the checkout form dynamically.
function createCheckoutForm() {
  // Check whether the checkout form already exists.
  const existingCheckout = document.querySelector("#checkout-section");

  if (existingCheckout) {
    return existingCheckout;
  }

  // Create a new section element.
  const checkoutSection = document.createElement("section");

  checkoutSection.id = "checkout-section";

  // Add the checkout HTML using a template literal.
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

  // Add the checkout section to the main element.
  document.querySelector("main").appendChild(checkoutSection);

  return checkoutSection;
}

// Open the checkout form.
function openCheckout() {
  // Do not allow checkout with an empty cart.
  if (state.cart.length === 0) {
    alert("Your cart is empty. Please add a product before checkout.");

    return;
  }

  // Create or retrieve the checkout form.
  const checkoutSection = createCheckoutForm();

  checkoutSection.style.display = "block";

  // Update the checkout total.
  const checkoutTotal = document.querySelector("#checkout-total");

  checkoutTotal.textContent =
    "Order Total: " + cartTotal().toLocaleString() + " ETB";

  // Smoothly scroll to the checkout section.
  checkoutSection.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });

  // Automatically focus on the name field.
  document.querySelector("#name").focus();
}

// Validate checkout form data.
function validateCheckout(data) {
  // Check name.
  if (!data.name.trim()) {
    return "Please enter your name.";
  }

  // Check phone using the regular expression.
  if (!PHONE.test(data.phone.trim())) {
    return "Enter a valid Ethiopian phone.";
  }

  // Check delivery area.
  if (!data.area) {
    return "Please select a delivery area.";
  }

  // Check that the cart is not empty.
  if (state.cart.length === 0) {
    return "Your cart is empty.";
  }

  // Check every cart item.
  for (const item of state.cart) {
    const quantity = Number(item.qty);
    const price = Number(item.price);

    // Check quantity.
    if (!Number.isFinite(quantity) || quantity <= 0) {
      return "Your cart contains an invalid quantity.";
    }

    // Check price.
    if (!Number.isFinite(price) || price < 0) {
      return "Your cart contains an invalid product price.";
    }
  }

  // Empty string means validation passed.
  return "";
}

// Create and save the customer's order.
function placeOrder(data) {
  // Create an order object.
  const order = {
    name: data.name.trim(),
    phone: data.phone.trim(),
    area: data.area,

    // map() creates a clean list of ordered items.
    items: state.cart.map(function (item) {
      return {
        id: item.id,
        name: item.name,
        price: Number(item.price),
        qty: Number(item.qty),
      };
    }),

    // Calculate the final order total.
    total: cartTotal(),

    // Store the order date and time.
    date: new Date().toISOString(),
  };

  // Save the completed order to localStorage.
  localStorage.setItem(ORDER_STORAGE_KEY, JSON.stringify(order));

  // Empty the cart after the order is placed.
  state.cart = [];

  // Save the empty cart.
  save();

  // Update the cart display.
  render();

  // Show the confirmation message.
  showOrderConfirmation(order);
}

// Display a checkout validation error.
function showCheckoutError(message) {
  const errorEl = document.querySelector("#form-error");

  if (!errorEl) {
    return;
  }

  errorEl.textContent = message;
}

// Display successful order confirmation.
function showOrderConfirmation(order) {
  const checkoutSection = document.querySelector("#checkout-section");

  if (!checkoutSection) {
    return;
  }

  // Replace the checkout form with the confirmation message.
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

// Handle checkout form submission.
document.addEventListener("submit", function (event) {
  // Ignore submissions from forms other than checkout.
  if (!event.target.matches("#checkout")) {
    return;
  }

  // Prevent the browser from refreshing the page.
  event.preventDefault();

  // Get the checkout form elements.
  const nameEl = document.querySelector("#name");

  const phoneEl = document.querySelector("#phone");

  const areaEl = document.querySelector("#area");

  // Collect the user's form data.
  const data = {
    name: nameEl.value,
    phone: phoneEl.value,
    area: areaEl.value,
  };

  // Get the first validation error.
  const error = validateCheckout(data);

  // Display the error if one exists.
  showCheckoutError(error);

  // Stop if validation fails.
  if (error) {
    // Focus the first invalid field.
    if (!data.name.trim()) {
      nameEl.focus();
    } else if (!PHONE.test(data.phone.trim())) {
      phoneEl.focus();
    } else {
      areaEl.focus();
    }

    return;
  }

  // Place the order if validation succeeds.
  placeOrder(data);
});

// Open checkout when the Checkout button is clicked.
checkoutButton.addEventListener("click", openCheckout);

// Handle Cancel Checkout and Continue Shopping.
document.addEventListener("click", function (event) {
  // Cancel checkout.
  if (event.target.matches("#cancel-checkout-button")) {
    const checkoutSection = document.querySelector("#checkout-section");

    if (checkoutSection) {
      checkoutSection.remove();
    }

    return;
  }

  // Continue shopping after a successful order.
  if (event.target.matches("#continue-shopping-button")) {
    const checkoutSection = document.querySelector("#checkout-section");

    if (checkoutSection) {
      checkoutSection.remove();
    }

    // Scroll back to the top of the page.
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  }
});

// Initialize the application.
async function init() {
  // Restore any previously saved cart.
  load();

  // Load products from JSON.
  await loadProducts();
}

// Start the application.
init();
