# Some Insights based on numbers


### Square of a Sorted Array
[-5,-4,-3,-2,-1,0,1,2,3,4,5]
- This can be easily squared and sorted but the complexity will be O(nlogn)
- To reduce the complexity it can be solved with double pointers
- Take L,R pointers pointing to first and last  element, compare their absolute value and append the square of the higheset to the end of the new array whose length same as the original array
- This method doesn't work the other way around i.e. compare the first and last element and append the smallest element at the front and keep going till last
- This is because, in sorted arrays with both negative and positive numbers, the smallest elements (closer to zero) don't necessarily represent the smallest squares.
