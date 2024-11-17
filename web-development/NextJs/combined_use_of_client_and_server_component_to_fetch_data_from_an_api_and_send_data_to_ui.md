### **Problem: `async/await` Not Supported in Client Components**

In Next.js, there is a distinction between **Server Components** and **Client Components**. Server Components are executed on the server and can handle asynchronous operations like `async/await` for data fetching. On the other hand, Client Components are rendered on the client and cannot directly use `async/await`.

Attempting to use `async/await` in Client Components results in the following error:

> `async/await` is not yet supported in Client Components, only Server Components. This error is often caused by accidentally adding `'use client'` to a module that was originally written for the server.

---

### **Cause of the Issue**
1. **Next.js Design**: 
   - Server Components are optimized for server-side rendering and can use `async/await` to fetch data.
   - Client Components, rendered in the browser, cannot handle asynchronous operations since the server has already rendered them by the time they reach the client.

2. **Mixing of Concerns**: If data fetching is attempted in a Client Component (e.g., a component marked with `'use client'`), it violates this separation of concerns.

---

### **Solution: Separation of Responsibilities**

To resolve this, you should:
1. **Fetch Data in Server Components**:
   - Use `async/await` to fetch data in a Server Component.
   - Pass the fetched data to Client Components as props.

2. **Render the UI in Client Components**:
   - Design the UI logic in a Client Component using the data passed from the Server Component.

---

### **Implementation**

#### **Step 1: Server Component for Data Fetching**
This is the component responsible for fetching data.

```jsx
// app/movies/[id]/page.jsx
import MovieDetails from "@/app/components/MovieDetails";

const Movie = async ({ params }) => {
    const { id } = params; // Extract the movie ID from the route parameters.

    // Fetch the movie data from the API
    const res = await fetch(`https://fakestoreapi.com/products/${id}`);
    const movie = await res.json();

    // Pass the fetched movie data to the Client Component
    return <MovieDetails movie={movie} />;
};

export default Movie;
```

---

#### **Step 2: Client Component for Rendering**
This component receives the fetched data as props and focuses on rendering the UI.

```jsx
// app/components/MovieDetails.jsx
'use client';

const MovieDetails = ({ movie }) => {
    // Render a fallback message if the movie is not found
    if (!movie) {
        return (
            <div className="flex items-center justify-center min-h-screen bg-gray-100">
                <h1 className="text-xl font-bold text-red-500">Movie not found!</h1>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-r from-blue-200 via-purple-300 to-pink-200 p-8">
            <div className="max-w-5xl mx-auto bg-white shadow-lg rounded-lg overflow-hidden">
                <div className="relative">
                    <img
                        src={movie.image}
                        alt={movie.title}
                        className="w-full h-96 object-cover"
                    />
                    <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-black via-transparent to-transparent p-4">
                        <h1 className="text-3xl font-bold text-white">{movie.title}</h1>
                        <p className="text-lg text-gray-200 mt-1">{movie.category}</p>
                    </div>
                </div>
            </div>
            <div className="max-w-5xl mx-auto bg-white shadow-lg rounded-lg mt-8 p-6">
                <h2 className="text-2xl font-bold mb-4">Details</h2>
                <p className="text-gray-700 mb-4">{movie.description}</p>
                <p className="text-lg font-semibold">Price: <span className="text-green-600">${movie.price}</span></p>
            </div>
        </div>
    );
};

export default MovieDetails;
```

---

### **Key Benefits of the Solution**
1. **Scalable Architecture**:
   - Clear separation of concerns: server handles data fetching, and client handles rendering.
2. **Improved Performance**:
   - Server Components render faster since they fetch data directly on the server.
3. **Future-Proof Code**:
   - Avoids potential breaking changes in Next.js by adhering to the separation of responsibilities.

---

### **Conclusion**
To handle `async/await` in Next.js, always perform data fetching in Server Components and pass the data to Client Components for rendering. This approach aligns with Next.js best practices, ensures smooth server-client rendering, and keeps your codebase organized and scalable.
