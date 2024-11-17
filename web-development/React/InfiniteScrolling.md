# Infinite Scrolling With Paginatino in React


1. Define state variables:
   - `data`: Array to store fetched items.
   - `page`: Current page number for pagination.
   - `loading`: Flag to indicate loading state.
   - `hasMore`: Boolean to check if more data exists on the server.

2. Create a function `fetchData`:
   - Make an API call using the current `page`:
     ```
     GET https://api.example.com/items?limit=10&page=${page}
     ```
   - Append fetched data to `data` state.
   - If no data is returned, set `hasMore` to `false`.

3. Use an `IntersectionObserver`:
   - Monitor a reference (`observerRef`) at the bottom of the page.
   - When the observer triggers, call `fetchData`.

4. Render items:
   - Map over `data` and render components for each item.

5. Display a loading spinner if `loading` is `true`.

6. Stop observing and display "No more items" if `hasMore` is `false`.

---

### Case 2: **API Does Not Support Pagination**

If the API doesn’t support pagination, you need to fetch all data initially and then paginate locally.

#### Pseudo-Code:
```jsx
1. Define state variables:
   - `allData`: Array to store all fetched items.
   - `visibleData`: Array to store currently visible items.
   - `batchSize`: Number of items to load at a time.
   - `loading`: Flag to indicate loading state.

2. Create a function `fetchAllData`:
   - Make an API call to fetch all items:
     ```
     GET https://api.example.com/items
     ```
   - Store the result in `allData` state.
   - Set the first `batchSize` items to `visibleData`.

3. Create a function `loadMoreData`:
   - Append the next `batchSize` items from `allData` to `visibleData`.

4. Use an `IntersectionObserver`:
   - Monitor a reference (`observerRef`) at the bottom of the page.
   - When the observer triggers, call `loadMoreData`.

5. Render items:
   - Map over `visibleData` and render components for each item.

6. Display a loading spinner if `loading` is `true`.

7. Stop observing and display "No more items" if `visibleData.length >= allData.length`.

---

### Shared React Component Structure:
```jsx
import { useState, useEffect, useRef } from 'react';

const InfiniteScrollComponent = ({ fetchUrl, isPaginated = false }) => {
    // States
    const [data, setData] = useState([]);
    const [allData, setAllData] = useState([]);
    const [visibleData, setVisibleData] = useState([]);
    const [page, setPage] = useState(1);
    const [loading, setLoading] = useState(false);
    const [hasMore, setHasMore] = useState(true);
    const observerRef = useRef(null);
    const batchSize = 10;

    // Fetch Data (API)
    const fetchData = async () => {
        if (loading || !hasMore) return;

        setLoading(true);
        try {
            const url = isPaginated
                ? `${fetchUrl}?limit=${batchSize}&page=${page}`
                : fetchUrl;

            const response = await fetch(url);
            const result = await response.json();

            if (isPaginated) {
                // Append new items
                setData((prev) => [...prev, ...result]);
                setPage((prev) => prev + 1);
                setHasMore(result.length > 0); // Stop if no more data
            } else {
                // Store all data and initialize visibleData
                setAllData(result);
                setVisibleData(result.slice(0, batchSize));
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    // Load More Data (Client-Side Pagination)
    const loadMoreData = () => {
        if (visibleData.length < allData.length) {
            const nextBatch = allData.slice(visibleData.length, visibleData.length + batchSize);
            setVisibleData((prev) => [...prev, ...nextBatch]);
        } else {
            setHasMore(false);
        }
    };

    // Observer Setup
    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) {
                if (isPaginated) {
                    fetchData();
                } else {
                    loadMoreData();
                }
            }
        }, { threshold: 1.0 });

        if (observerRef.current) observer.observe(observerRef.current);
        return () => observer.disconnect();
    }, [data, allData, visibleData]);

    // Initial Data Fetch
    useEffect(() => {
        fetchData();
    }, []);

    return (
        <div>
            <div>
                {(isPaginated ? data : visibleData).map((item, index) => (
                    <div key={item.id || index}>{/* Render your item here */}</div>
                ))}
            </div>
            {loading && <div>Loading...</div>}
            <div ref={observerRef} />
            {!hasMore && <div>No more items</div>}
        </div>
    );
};

export default InfiniteScrollComponent;
