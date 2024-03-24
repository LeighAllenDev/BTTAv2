document.addEventListener('DOMContentLoaded', function() {
    const bundleSelect = document.querySelector("#id_bundle");
    let foodTokensRemaining = 0;
    let drinkTokensRemaining = 0;

    // Event listener for when the bundle selection changes
    bundleSelect.addEventListener('change', function() {
        const bundleId = this.value;
        // Fetch details for the selected bundle using the specified endpoint
        fetchBundleDetails(bundleId);
    });
});

// Function to fetch details for the selected bundle
function fetchBundleDetails(bundleId) {
    // Use the endpoint with the selected bundle's ID
    console.log(bundleId)
    fetch(`/bundles/api/bundles/${bundleId}/`)
        .then(response => {
            if (!response.ok) throw new Error('Network response was not ok');
            console.log(response)
            return response.json();
        })
        .then(data => {
            console.log(data)
            foodTokensRemaining = data.food_tokens; // Total food tokens available from the bundle
            drinkTokensRemaining = data.drink_tokens;
            // Assuming 'data' contains properties for food_items, drink_items, and tokens
            // Update the dropdowns for food and drink choices
            updateDropdown('id_food_choice', data.food_items);
            updateDropdown('id_drink_choice', data.drink_items);

            initFoodDropdown(data.food_items);
            initDrinkDropdown(data.drink_items);
            // Update tokens display (if applicable)
            // You might need a function here to handle tokens display update if you're tracking tokens in the UI
        })
        .catch(error => console.error('Error fetching bundle details:', error));
}

function initFoodDropdown(foodItems) {
    const foodDropdownContainer = document.getElementById('food-dropdown-container');
    foodDropdownContainer.innerHTML = ''; // Clear previous dropdowns

    // Create a new dropdown for food choices
    let dropdownHTML = '<select id="food_choice" name="food_choice">';
    foodItems.forEach(item => {
        dropdownHTML += `<option value="${item.id}" data-tokens="${item.tokens_required}">${item.name} - Tokens: ${item.tokens_required}</option>`;
    });
    dropdownHTML += '</select>';

    foodDropdownContainer.innerHTML = dropdownHTML;

}

function updateDropdown(fieldId, items) {
    const dropdown = document.querySelector(`#${fieldId}`);
    dropdown.innerHTML = ''; // Clear previous options
    items.forEach(item => {
        // Create a new option element for each item and add it to the dropdown
        const option = new Option(item.name, item.id); // Assuming each item has 'name' and 'id' fields
        dropdown.add(option);
    });
}
