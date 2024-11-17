### Infinite Scroll with Separate Code for Paginated and Non-Paginated APIs

Here’s how to handle **paginated** and **non-paginated** APIs with clear separation. Each use case has its own implementation.

---

#### 1. **Paginated API** Example Code (`PaginatedInfiniteScroll.jsx`)

For APIs supporting pagination with `page` and `limit` parameters.

```jsx
import { useState, useEffect, useRef } from 'react';

const PaginatedInfiniteScroll = ({ fetchUrl }) => {
    const [data, setData] = useState([]); // Data fetched from the API
    const [page, setPage] = useState(1); // Current page
    const [loading, setLoading] = useState(false); // Loading indicator
    const [hasMore, setHasMore] = useState(true); // Check if more data exists
    const observerRef = useRef(null); // Intersection Observer reference

    // Fetch data for the current page
    const fetchData = async () => {
        if (loading || !hasMore) return;

        setLoading(true);
        try {
            const response = await fetch(`${fetchUrl}?limit=10&page=${page}`);
            const result = await response.json();
            setData((prev) => [...prev, ...result]);
            setPage((prev) => prev + 1);
            setHasMore(result.length > 0); // Stop fetching if no data
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    // Intersection Observer setup
    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) fetchData();
        }, { threshold: 1.0 });

        if (observerRef.current) observer.observe(observerRef.current);
        return () => observer.disconnect();
    }, [page, hasMore]);

    return (
        <div className="infinite-scroll">
            <div className="data-grid">
                {data.map((item, index) => (
                    <div key={item.id || index} className="data-card">
                        <h3>{item.title || `Item ${index + 1}`}</h3>
                        <p>{item.description || 'No description available.'}</p>
                    </div>
                ))}
            </div>

            {loading && <div className="loading">Loading...</div>}
            <div ref={observerRef} className="observer-trigger" />
            {!hasMore && <div className="end-message">No more items to load</div>}
        </div>
    );
};

export default PaginatedInfiniteScroll;
```

---

#### 2. **Non-Paginated API** Example Code (`NonPaginatedInfiniteScroll.jsx`)

For APIs that return all data at once, but you want to load items in batches.

```jsx
import { useState, useEffect, useRef } from 'react';

const NonPaginatedInfiniteScroll = ({ fetchUrl }) => {
    const [allData, setAllData] = useState([]); // Complete dataset
    const [visibleData, setVisibleData] = useState([]); // Currently visible items
    const [loading, setLoading] = useState(false); // Loading indicator
    const [hasMore, setHasMore] = useState(true); // Check if more data exists
    const observerRef = useRef(null); // Intersection Observer reference
    const batchSize = 10; // Number of items to show per batch

    // Fetch all data once
    const fetchAllData = async () => {
        setLoading(true);
        try {
            const response = await fetch(fetchUrl);
            const result = await response.json();
            setAllData(result);
            setVisibleData(result.slice(0, batchSize)); // Show initial batch
        } catch (error) {
            console.error('Error fetching data:', error);
        } finally {
            setLoading(false);
        }
    };

    // Load the next batch of data
    const loadMoreData = () => {
        const nextBatch = allData.slice(visibleData.length, visibleData.length + batchSize);
        setVisibleData((prev) => [...prev, ...nextBatch]);
        if (visibleData.length + batchSize >= allData.length) setHasMore(false);
    };

    // Intersection Observer setup
    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) loadMoreData();
        }, { threshold: 1.0 });

        if (observerRef.current) observer.observe(observerRef.current);
        return () => observer.disconnect();
    }, [visibleData, allData]);

    // Initial fetch
    useEffect(() => {
        fetchAllData();
    }, []);

    return (
        <div className="infinite-scroll">
            <div className="data-grid">
                {visibleData.map((item, index) => (
                    <div key={item.id || index} className="data-card">
                        <h3>{item.title || `Item ${index + 1}`}</h3>
                        <p>{item.description || 'No description available.'}</p>
                    </div>
                ))}
            </div>

            {loading && <div className="loading">Loading...</div>}
            <div ref={observerRef} className="observer-trigger" />
            {!hasMore && <div className="end-message">No more items to load</div>}
        </div>
    );
};

export default NonPaginatedInfiniteScroll;
```

---

### Key Differences Between the Two Approaches:

| Feature                | Paginated API                                   | Non-Paginated API                              |
|------------------------|------------------------------------------------|-----------------------------------------------|
| **Data Fetching**      | Fetches a small chunk of data (e.g., per page). | Fetches the entire dataset in one request.    |
| **Load More Logic**    | Fetches next page via API (`?page=n`).          | Loads next batch from locally stored data.    |
| **Performance**        | API handles pagination; less initial overhead. | Client handles pagination; heavier initially. |
| **Use Case**           | Preferred when the API supports pagination.    | Useful when the API doesn’t support paging.   |

---

### Notes

1. **Paginated API**:
   - Ideal for large datasets because it avoids fetching unnecessary data.
   - Ensure your backend supports pagination (with `page` and `limit` parameters).

2. **Non-Paginated API**:
   - Simulates infinite scroll by managing batches on the client.
   - Suitable for small-to-medium datasets since all data is fetched upfront.

3. **Styling**:
   - Customize `.loading`, `.end-message`, `.data-card`, and `.observer-trigger` for a polished UI.

4. **Error Handling**:
   - Add error messages or fallback states in case of fetch failures.


### Pseudo Code for Infinite Scroll with Paginated and Non-Paginated APIs

Below is the pseudo code for both cases: **Paginated API** and **Non-Paginated API**.

---

### 1. **Paginated API** Pseudo Code

For APIs supporting pagination with `page` and `limit` parameters:

```
Component: PaginatedInfiniteScroll

State Variables:
  data: Holds the fetched data
  page: Current page number (initially 1)
  loading: A flag to track if data is currently being fetched
  hasMore: A flag to indicate if there are more pages to load

On Mount:
  Fetch initial data for the first page:
    - Fetch data from API with page=1 and limit=10
    - Store the data in 'data' state
    - Increment the page number by 1

When Scroll Near Bottom:
  1. Check if loading is false and hasMore is true.
  2. If true:
    - Set loading to true
    - Fetch the next page of data (e.g., page 2)
    - Append the new data to the existing data
    - Increment the page number by 1
    - If the fetched data length is less than limit, set hasMore to false (no more pages).

Display the content:
  - Map through 'data' state and render each item as a card.
  - Display a loading spinner when loading is true.
  - Show a message if there is no more data to load.

End:
  - Repeat fetching and appending data as the user scrolls down.
```

---

### 2. **Non-Paginated API** Pseudo Code

For APIs returning all data at once, but simulating infinite scroll by loading items in batches.

```
Component: NonPaginatedInfiniteScroll

State Variables:
  allData: Holds the entire fetched data (loaded once from the API)
  visibleData: Holds the data that is currently visible on the screen (initially a batch of 10 items)
  loading: A flag to track if data is currently being fetched
  hasMore: A flag to indicate if more data is available to show (based on batch size)

On Mount:
  1. Fetch all data from the API.
  2. Store all the data in 'allData'.
  3. Set the first batch (10 items) to be displayed in 'visibleData'.

When Scroll Near Bottom:
  1. Check if loading is false and hasMore is true.
  2. If true:
    - Set loading to true
    - Get the next batch of items from 'allData' (e.g., items 11-20).
    - Append the new batch of items to 'visibleData'.
    - If all items from 'allData' are shown, set hasMore to false.

Display the content:
  - Map through 'visibleData' state and render each item as a card.
  - Display a loading spinner when loading is true.
  - Show a message if there is no more data to load.

End:
  - Keep loading the next batch of data when the user scrolls down until all data is loaded.
```

---

### Key Differences in Pseudo Code:

| Feature                | Paginated API                                | Non-Paginated API                             |
|------------------------|----------------------------------------------|----------------------------------------------|
| **Data Fetching**      | Fetch a small chunk of data (page-by-page).  | Fetch all data at once and manage batches.   |
| **Load More Logic**    | Increment page number and fetch next page.   | Manage the batch and load more items from local data. |
| **Performance**        | Efficient with large datasets; minimizes network calls. | Potentially slower for large datasets but can manage small-to-medium sets effectively. |
| **Data Structure**     | Stored in pages, fetched progressively.      | Stored all at once, divided into batches.    |

---

