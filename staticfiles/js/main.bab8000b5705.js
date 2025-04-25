// Preloader
setTimeout(() => {
    const preloader = document.getElementById('preloader');
    preloader.style.display = 'none';
}, 2000);

const itemsList = document.getElementById("items-list");
const addItemForm = document.getElementById("add-item-form");
const editItemForm = document.getElementById("edit-item-form");

document.addEventListener("DOMContentLoaded", function() {
    const cardContainer = document.getElementById("card-container");
    const taskCards = document.getElementById("task-cards");
    const tableContainer = document.querySelector(".table-container");
    const showCardsBtn = document.getElementById("show-cards-btn");
    const showTableBtn = document.getElementById("show-table-btn");
    var displayType;

    // Fetch and display items
    function fetchItems(displayType = 'table') {
        fetch('http://127.0.0.1:8000/api/items/')
            .then(response => response.json())
            .then(data => {
                if (displayType === 'table') {
                    itemsList.innerHTML = '';
                    data.forEach((item, index) => {
                        const row = document.createElement("tr");
                        row.innerHTML = `
                            <td>${index + 1}</td>
                            <td>${item.name}</td>
                            <td>${item.description}</td>
                            <td>${item.status}</td>
                            <td>${item.priority}</td>
                            <td>${item.due_date}</td>
                            <td>
                                <button class="edit-btn" data-id="${item.id}">Edit</button>
                                <button class="delete-btn" data-id="${item.id}">Delete</button>
                            </td>
                        `;
                        itemsList.appendChild(row);
                    });
                } else if (displayType === 'cards') {
                    taskCards.innerHTML = '';
                    data.forEach(item => {
                        const card = document.createElement("div");
                        card.classList.add("card");
                        card.innerHTML = `
                            <h3>${item.name}</h3>
                            <p>${item.description}</p>
                            <p>Status: ${item.status}</p>
                            <p>Priority: ${item.priority}</p>
                            <p>Due: ${item.due_date}</p>
                            <button class="edit-btn" data-id="${item.id}">Edit</button>
                            <button class="delete-btn" data-id="${item.id}">Delete</button>
                        `;
                        taskCards.appendChild(card);
                    });
                }

                // Add event listeners for edit and delete buttons
                document.querySelectorAll('.edit-btn').forEach(btn => btn.addEventListener('click', handleEdit));
                document.querySelectorAll('.delete-btn').forEach(btn => btn.addEventListener('click', handleDelete));
            })
            .catch(error => console.error('Error fetching items:', error));
    }

    // Show card view
    showCardsBtn.addEventListener("click", function() {
        tableContainer.style.display = 'none';
        cardContainer.style.display = 'block';
        displayType = 'cards';
        fetchItems(displayType);
    });

    // Show table view
    showTableBtn.addEventListener("click", function() {
        cardContainer.style.display = 'none';
        tableContainer.style.display = 'block';
        displayType = 'table'
        fetchItems(displayType);
    });

    // Add a new item
    addItemForm.addEventListener("submit", function(e) {
        e.preventDefault();
        const name = document.getElementById("name").value;
        const description = document.getElementById("description").value;
        const status = document.getElementById("status").value;
        const priority = document.getElementById("priority").value;
        const due_date = document.getElementById("due_date").value;

        const newItem = { name, description, status, priority, due_date };

        fetch('http://127.0.0.1:8000/api/items/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')  
            },
            body: JSON.stringify(newItem)
        })
        .then(() => fetchItems(displayType))
        .catch(error => console.error("Error adding item:", error));
    });

    // Handle edit item
    function handleEdit(event) {
        const id = event.target.getAttribute("data-id");

        fetch(`http://127.0.0.1:8000/api/items/${id}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById("edit-id").value = data.id;
                document.getElementById("edit-name").value = data.name;
                document.getElementById("edit-description").value = data.description;
                document.getElementById("edit-status").value = data.status;
                document.getElementById("edit-priority").value = data.priority;
                document.getElementById("edit-due_date").value = data.due_date;

                addItemForm.style.display = "none";
                editItemForm.style.display = "flex";
            })
            .catch(error => console.error("Error fetching item:", error));
    }

    // Update item
    editItemForm.addEventListener("submit", function(e) {
        e.preventDefault();
        const id = document.getElementById("edit-id").value;
        const updatedItem = {
            name: document.getElementById("edit-name").value,
            description: document.getElementById("edit-description").value,
            status: document.getElementById("edit-status").value,
            priority: document.getElementById("edit-priority").value,
            due_date: document.getElementById("edit-due_date").value
        };

        fetch(`http://127.0.0.1:8000/api/items/${id}/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie('csrftoken')
            },
            body: JSON.stringify(updatedItem)
        })
        .then(() => {
            fetchItems(displayType);
            addItemForm.style.display = "flex";
            editItemForm.style.display = "none";
        })
        .catch(error => console.error("Error updating item:", error));
    });

    // Delete item
    function handleDelete(event) {
        const id = event.target.getAttribute("data-id");

        fetch(`http://127.0.0.1:8000/api/items/${id}/`, {
            method: "DELETE",
            headers: {
                "X-CSRFToken": getCookie('csrftoken')
            }
        })
        .then(() => fetchItems(displayType))
        .catch(error => console.error("Error deleting item:", error));
    }

    // Fetch CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    fetchItems(displayType);  // Initial fetch
});