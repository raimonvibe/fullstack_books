document.addEventListener('DOMContentLoaded', function() {
    const bookGrid = document.getElementById('book-grid');
    if (bookGrid) {
        fetchBooks();
    } else {
        console.log('No book-grid element found on this page. Skipping fetchBooks.');
    }

    const addBookForm = document.getElementById('add-book-form');
    if (addBookForm) {
        addBookForm.addEventListener('submit', addBook);
    }

    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');
    if (searchInput && searchButton) {
        searchInput.addEventListener('input', debounce(handleSearch, 300));
        searchButton.addEventListener('click', handleSearch);
    }
});

function fetchBooks(searchQuery = '') {
    let url = '/api/books';
    if (searchQuery) {
        url += `?search=${encodeURIComponent(searchQuery)}`;
    }
    fetch(url)
        .then(response => response.json())
        .then(books => {
            const bookGrid = document.getElementById('book-grid');
            if (bookGrid) {
                bookGrid.innerHTML = '';
                books.forEach(book => {
                    const bookElement = createBookElement(book);
                    bookGrid.appendChild(bookElement);
                });
            } else {
                console.log(document.body.innerHTML);
                console.error('Error: book-grid element not found');
            }
        })
        .catch(error => console.error('Error:', error));
}

function createBookElement(book) {
    const div = document.createElement('div');
    div.className = 'book-item';
    div.innerHTML = `
        <h3>${book.title}</h3>
        <p>Author: ${book.author}</p>
        <p>Year: ${book.publication_year || 'N/A'}</p>
        <button onclick="showBookDetails(${book.id})">Details</button>
    `;
    return div;
}

function addBook(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const bookData = Object.fromEntries(formData.entries());

    fetch('/api/books', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(bookData),
    })
    .then(response => response.json())
    .then(() => {
        fetchBooks();
        event.target.reset();
    })
    .catch(error => console.error('Error:', error));
}

function handleSearch() {
    const searchQuery = document.getElementById('search-input').value;
    fetchBooks(searchQuery);
}

function showBookDetails(id) {
    window.location.href = `/book/${id}`;
}

function debounce(func, delay) {
    let debounceTimer;
    return function() {
        const context = this;
        const args = arguments;
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => func.apply(context, args), delay);
    }
}
