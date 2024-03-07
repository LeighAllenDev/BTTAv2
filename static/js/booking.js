document.addEventListener('DOMContentLoaded', function() {
    const bundleSelect = document.querySelector("#id_bundle"); // Adjust the selector as needed

    bundleSelect.addEventListener('change', function() {
        const bundleId = this.value;
        fetchMenuItemsForBundle(bundleId);
    });
});

function fetchMenuItemsForBundle(bundleId) {
    // Adjust the URL to match your API endpoint
    fetch(`/api/bundle-menu-items/${bundleId}/`)  
        .then(response => response.json())
        .then(data => {
            updateDropdown('id_food_choice', data.food_items);
            updateDropdown('id_drink_choice', data.drink_items);
        })
        .catch(error => console.error('Error fetching menu items:', error));
}

function updateDropdown(fieldId, items) {
    const dropdown = document.querySelector(`#${fieldId}`);
    dropdown.innerHTML = ''; // Clear existing options
    items.forEach(item => {
        const option = new Option(item.name, item.id);
        dropdown.appendChild(option);
    });
}
