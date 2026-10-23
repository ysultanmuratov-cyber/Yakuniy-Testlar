<!DOCTYPE html>
<html lang="uz">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Zamonaviy Online Do'kon</title>
  <style>
    :root {
      --primary: #2563eb;
      --primary-hover: #1d4ed8;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    body {
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }

    header {
      background-color: var(--card-bg);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .header-container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: 700;
      color: var(--primary);
      text-decoration: none;
    }

    .search-box input {
      padding: 0.5rem 1rem;
      border: 1px solid var(--border);
      border-radius: 20px;
      width: 250px;
      outline: none;
    }

    .cart-btn {
      position: relative;
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.6rem 1.2rem;
      border-radius: 8px;
      cursor: pointer;
      font-weight: 600;
    }

    .cart-count {
      position: absolute;
      top: -8px;
      right: -8px;
      background: #ef4444;
      color: white;
      border-radius: 50%;
      padding: 2px 6px;
      font-size: 0.75rem;
    }

    main {
      max-width: 1200px;
      margin: 2rem auto;
      padding: 0 2rem;
    }

    .categories {
      display: flex;
      gap: 0.5rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }

    .cat-btn {
      padding: 0.5rem 1rem;
      border: 1px solid var(--border);
      background: var(--card-bg);
      border-radius: 20px;
      cursor: pointer;
      font-weight: 500;
    }

    .cat-btn.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 1.5rem;
    }

    .product-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow);
      transition: transform 0.2s;
    }

    .product-card:hover {
      transform: translateY(-4px);
    }

    .product-img {
      width: 100%;
      height: 180px;
      object-fit: cover;
      border-radius: 8px;
      margin-bottom: 1rem;
    }

    .product-title {
      font-size: 1.1rem;
      font-weight: 600;
      margin-bottom: 0.5rem;
    }

    .product-price {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--primary);
      margin-top: auto;
      margin-bottom: 1rem;
    }

    .add-to-cart {
      background: var(--primary);
      color: white;
      border: none;
      padding: 0.6rem;
      border-radius: 6px;
      cursor: pointer;
      font-weight: 600;
      width: 100%;
    }

    .add-to-cart:hover {
      background: var(--primary-hover);
    }

    /* Modal for Cart */
    .cart-modal {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.5);
      justify-content: flex-end;
      z-index: 1000;
    }

    .cart-modal.open {
      display: flex;
    }

    .cart-content {
      background: var(--card-bg);
      width: 100%;
      max-width: 400px;
      height: 100%;
      padding: 2rem;
      display: flex;
      flex-direction: column;
    }

    .cart-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 1rem;
    }

    .close-btn {
      background: none;
      border: none;
      font-size: 1.5rem;
      cursor: pointer;
    }

    .cart-items {
      flex: 1;
      overflow-y: auto;
    }

    .cart-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.5rem;
    }

    .cart-footer {
      border-top: 1px solid var(--border);
      padding-top: 1rem;
      margin-top: auto;
    }

    .checkout-btn {
      width: 100%;
      background: #10b981;
      color: white;
      border: none;
      padding: 0.8rem;
      border-radius: 8px;
      font-size: 1rem;
      font-weight: 600;
      cursor: pointer;
      margin-top: 1rem;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-container">
      <a href="#" class="logo">TechStore</a>
      <div class="search-box">
        <input type="text" id="searchInput" placeholder="Mahsulotlarni qidirish..." oninput="filterProducts()">
      </div>
      <button class="cart-btn" onclick="toggleCart()">
        Savatcha <span class="cart-count" id="cartCount">0</span>
      </button>
    </div>
  </header>

  <main>
    <div class="categories" id="categoryButtons">
      <button class="cat-btn active" onclick="filterCategory('all', this)">Barchasi</button>
      <button class="cat-btn" onclick="filterCategory('phone', this)">Telefonlar</button>
      <button class="cat-btn" onclick="filterCategory('laptop', this)">Noutbuklar</button>
      <button class="cat-btn" onclick="filterCategory('acc', this)">Aksessuarlar</button>
    </div>

    <div class="products-grid" id="productGrid"></div>
  </main>

  <!-- Savatcha Modali -->
  <div class="cart-modal" id="cartModal">
    <div class="cart-content">
      <div class="cart-header">
        <h2>Xarid Savatchasi</h2>
        <button class="close-btn" onclick="toggleCart()">&times;</button>
      </div>
      <div class="cart-items" id="cartItems"></div>
      <div class="cart-footer">
        <h3>Jami: <span id="cartTotal">$0</span></h3>
        <button class="checkout-btn" onclick="checkout()">Buyurtma berish</button>
      </div>
    </div>
  </div>

  <script>
    const products = [
      { id: 1, name: "iPhone 15 Pro", category: "phone", price: 999, img: "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=400" },
      { id: 2, name: "MacBook Air M2", category: "laptop", price: 1199, img: "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=400" },
      { id: 3, name: "AirPods Pro 2", category: "acc", price: 249, img: "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=400" },
      { id: 4, name: "Samsung Galaxy S24", category: "phone", price: 899, img: "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=400" },
      { id: 5, name: "Dell XPS 13", category: "laptop", price: 1299, img: "https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=400" },
      { id: 6, name: "Apple Watch Series 9", category: "acc", price: 399, img: "https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=400" }
    ];

    let cart = [];
    let currentCategory = 'all';

    function renderProducts(items) {
      const grid = document.getElementById('productGrid');
      grid.innerHTML = items.map(p => `
        <div class="product-card">
          <img src="${p.img}" alt="${p.name}" class="product-img">
          <h3 class="product-title">${p.name}</h3>
          <div class="product-price">$${p.price}</div>
          <button class="add-to-cart" onclick="addToCart(${p.id})">Savatga qo'shish</button>
        </div>
      `).join('');
    }

    function addToCart(id) {
      const product = products.find(p => p.id === id);
      const existing = cart.find(item => item.id === id);

      if (existing) {
        existing.qty++;
      } else {
        cart.push({ ...product, qty: 1 });
      }

      updateCart();
    }

    function updateCart() {
      const cartItems = document.getElementById('cartItems');
      const cartCount = document.getElementById('cartCount');
      const cartTotal = document.getElementById('cartTotal');

      cartCount.innerText = cart.reduce((acc, item) => acc + item.qty, 0);

      if (cart.length === 0) {
        cartItems.innerHTML = '<p>Savatchangiz bo\'sh.</p>';
        cartTotal.innerText = '$0';
        return;
      }

      cartItems.innerHTML = cart.map(item => `
        <div class="cart-item">
          <div>
            <strong>${item.name}</strong>
            <div>$${item.price} x ${item.qty}</div>
          </div>
          <div>
            <button onclick="changeQty(${item.id}, -1)">-</button>
            <button onclick="changeQty(${item.id}, 1)">+</button>
          </div>
        </div>
      `).join('');

      const total = cart.reduce((acc, item) => acc + item.price * item.qty, 0);
      cartTotal.innerText = `$${total}`;
    }

    function changeQty(id, delta) {
      const item = cart.find(i => i.id === id);
      if (!item) return;

      item.qty += delta;
      if (item.qty <= 0) {
        cart = cart.filter(i => i.id !== id);
      }
      updateCart();
    }

    function toggleCart() {
      document.getElementById('cartModal').classList.toggle('open');
    }

    function filterCategory(category, btn) {
      currentCategory = category;
      document.querySelectorAll('.cat-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterProducts();
    }

    function filterProducts() {
      const query = document.getElementById('searchInput').value.toLowerCase();
      const filtered = products.filter(p => {
        const matchesCategory = currentCategory === 'all' || p.category === currentCategory;
        const matchesQuery = p.name.toLowerCase().includes(query);
        return matchesCategory && matchesQuery;
      });
      renderProducts(filtered);
    }

    function checkout() {
      if (cart.length === 0) {
        alert("Savatcha bo'sh!");
        return;
      }
      alert("Xaridingiz uchun rahmat! Buyurtmangiz qabul qilindi.");
      cart = [];
      updateCart();
      toggleCart();
    }

    // Boshlang'ich yuklanish
    renderProducts(products);
  </script>
</body>
</html>
