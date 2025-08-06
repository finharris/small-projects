import React from "react";
import { convertToStacks } from "../utils/converter";

const ItemList = ({ items, markCollected, deleteItem, clearList }) => {
  // Sort: uncollected by quantity desc, collected at bottom
  const sorted = [...items].sort((a, b) => {
    if (a.collected === b.collected) {
      return b.quantity - a.quantity;
    }
    return a.collected ? 1 : -1;
  });

  return (
    <div className='item-list-container'>
      <h2>Required items</h2>
      <ul className='item-list'>
        {sorted.map((item, idx) => {
          const { stacks, remainder } = convertToStacks(item.quantity);
          return (
            <li
              key={idx}
              className={item.collected ? "collected" : ""}
              onClick={() => markCollected(items.indexOf(item))}
              style={{ cursor: "pointer", position: "relative" }}>
              <b>{item.name}</b>: {stacks} Stacks {remainder} Items ({item.quantity})
              <button
                onClick={(e) => {
                  e.stopPropagation();
                  deleteItem(items.indexOf(item));
                }}
                aria-label='Delete'>
                ×
              </button>
            </li>
          );
        })}
      </ul>
      <button className='button clear-list-button' onClick={clearList}>
        Clear list
      </button>
    </div>
  );
};

export default ItemList;
