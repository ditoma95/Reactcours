import { useState } from "react";
// import {SearchBar} from './components/searchbar';
// import {ProductTable} from '../components/ProductTable';

export function FilterableProductTable({ products }) {
    const [filterText, setFilterText] = useState('');
    const [inStockOnly, setInStockOnly] = useState(false);
  
    return (
      <div>
        <SearchBar 
          filterText={filterText} 
          inStockOnly={inStockOnly} 
          onFilterTextChange={setFilterText} 
          onInStockOnlyChange={setInStockOnly} />
        <ProductTable 
          products={products} 
          filterText={filterText}
          inStockOnly={inStockOnly} />
      </div>
    );
}
  
