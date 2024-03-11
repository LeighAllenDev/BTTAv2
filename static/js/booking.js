document.addEventListener('DOMContentLoaded', function() {
    const bundleSelectElement = document.getElementById('bundle-select');

    bundleSelectElement.addEventListener('change', function() {
        const categoryId = this.value; // Assuming the bundle's value is the category ID for simplicity
        fetchMenuItems(categoryId);
    });
});

function fetchMenuItems(categoryId) {
    fetch(`/api/menu-items/${categoryId}/`)
        .then(response => response.json())
        .then(data => {
            updateMenuItemsDropdown(data.menu_items);
        })
        .catch(error => console.error('Error fetching menu items:', error));
}

function updateMenuItemsDropdown(menuItems) {
    const menuItemsDropdown = document.getElementById('menu-items-dropdown');
    menuItemsDropdown.innerHTML = ''; // Clear existing options

    menuItems.forEach(item => {
        let optionElement = new Option(item.name, item.id);
        menuItemsDropdown.appendChild(optionElement);
    });
}
