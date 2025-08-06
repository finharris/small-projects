import React, { useState } from 'react';

const ItemForm = ({ addItem }) => {
  const [itemName, setItemName] = useState('');
  const [itemQuantity, setItemQuantity] = useState(1);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (itemName.trim() === '') return;

    addItem({ name: itemName, quantity: parseInt(itemQuantity) });
    setItemName('');
    setItemQuantity(1);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Item Name"
        value={itemName}
        onChange={(e) => setItemName(e.target.value)}
        required
      />
      <input
        type="number"
        min="1"
        value={itemQuantity}
        onChange={(e) => setItemQuantity(e.target.value)}
      />
      <button type="submit">Add Item</button>
    </form>
  );
};

export default ItemForm;