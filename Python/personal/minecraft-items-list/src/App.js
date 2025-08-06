import React, { useState } from "react";
import ItemForm from "./components/ItemForm";
import ItemList from "./components/ItemList";

const App = () => {
  const [items, setItems] = useState([]);

  const addItem = (item) => {
    setItems([...items, item]);
  };

  const markCollected = (idx) => {
    const updated = items.map((item, i) =>
      i === idx ? { ...item, collected: !item.collected } : item
    );
    setItems(updated);
  };

  return (
    <div>
      <h1>Minecraft Items List</h1>
      <ItemForm addItem={addItem} />
      <ItemList items={items} markCollected={markCollected} />
      {/* <StackConverter items={items} /> */}
    </div>
  );
};

export default App;
