// Import necessary React library and useState hook
import React, { useState } from 'react';

// Define the ItemList functional component
function ItemList() {
    // useState hook for managing the list of items
    const [items, setItems] = useState([]);
    // useState hook for managing the current input value for a new item
    const [newItem, setNewItem] = useState('');

    // Function to add a new item to the list
    const addItem = () => {
        // Prevent adding an empty item
        if (!newItem) return;
        // Add the new item to the items array and reset the input field
        setItems([...items, newItem]);
        setNewItem('');
    };

    // Function to remove an item from the list based on its index
    const removeItem = index => {
        // Filter out the item at the given index and update the items array
        const newItems = items.filter((item, i) => i !== index);
        setItems(newItems);
    };

    // Render the component
    return (
        <div>
            {/* Input field for adding a new item */}
            <input 
                type="text" 
                value={newItem} // Controlled input using newItem state
                onChange={(e) => setNewItem(e.target.value)} // Update state on input change
                placeholder="Enter new item"
            />
            {/* Button to add the new item to the list */}
            <button onClick={addItem}>Add Item</button>
            {/* List of items */}
            <ul>
                {items.map((item, index) => (
                    // Map each item to an li element
                    <li key={index}>
                        {item} {/* Display item */}
                        {/* Button to remove the item from the list */}
                        <button onClick={() => removeItem(index)}>Remove</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

// Export the ItemList component for use in other parts of the app
export default ItemList;

