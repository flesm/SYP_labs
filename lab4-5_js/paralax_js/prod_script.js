class Product {
    constructor(name, price, image) {
        this.name = name;
        this.price = price;
        this.image = image;
    }

    addToPage() {
        const productsDiv = document.getElementById('products');
        const productDiv = document.createElement('div');
        productDiv.className = 'product';

        const img = document.createElement('img');
        img.src = this.image;
        productDiv.appendChild(img);

        const namePara = document.createElement('p');
        namePara.textContent = this.name;
        namePara.classList.add('product-name');
        productDiv.appendChild(namePara);

        const pricePara = document.createElement('p');
        pricePara.textContent = this.price;
        pricePara.classList.add('product-price');
        productDiv.appendChild(pricePara);

        const addButton = document.createElement('button');
        addButton.textContent = 'В корзину';
        addButton.addEventListener('click', () => this.addToCart());
        productDiv.appendChild(addButton);

        const removeButton = document.createElement('button');
        removeButton.textContent = 'Удалить';
        removeButton.addEventListener('click', () => {
            productDiv.remove();
            this.removeFromCart();
        });
        productDiv.appendChild(removeButton);

        const editButton = document.createElement('button');
        editButton.textContent = 'Изменить';
        editButton.addEventListener('click', () => this.editProduct());
        productDiv.appendChild(editButton);

        productsDiv.appendChild(productDiv);
    }

    addToCart() {
        const cartDiv = document.getElementById('cart');

        const cartItem = document.createElement('div');
        cartItem.textContent = `${this.name} - ${this.price}`;

        const removeButton = document.createElement('button');
        removeButton.textContent = 'Удалить';
        removeButton.addEventListener('click', () => {
            cartItem.remove();
            this.removeFromPage();
        });

        cartItem.appendChild(removeButton);

        cartDiv.appendChild(cartItem);
    }

    editProduct() {
        const newName = prompt('Введите новое название товара:');
        const newPrice = prompt('Введите новую стоимость товара:');
        const newImage = prompt('Введите новую ссылку на изображение товара:');

        this.name = newName;
        this.price = newPrice;
        this.image = newImage;

        const productDiv = document.querySelector('.product img[src="' + this.image + '"]').parentNode;
        productDiv.querySelector('.product-name').textContent = this.name;
        productDiv.querySelector('.product-price').textContent = this.price;
    }
}

const products = [];

function addProductToPage() {
    const name = prompt('Введите название товара:');
    const price = prompt('Введите стоимость товара:');
    const image = prompt('Введите ссылку на изображение товара:');

    const newProduct = new Product(name, '$'+price, image);
    newProduct.addToPage();
    products.push(newProduct);
}

document.getElementById('add-product-btn').addEventListener('click', addProductToPage);