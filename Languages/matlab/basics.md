# Matlab Basics




### Making variables
```matlab
x = 5 % single variable of type double
y = [1,2,3,4,5] % make a row vector
z = [1;2;3;4;5] 
```



## Lab code


### Mix two arrays

```
x1 = [1, 2, 3, 4, 5];
x2 = [5, 4, 3, 2, 1];
x = [];
p1 = 1;
p2 = 1;
i = 0;

while (p1 <= length(x1) || p2 <= length(x2))
    if mod(i, 2) == 0
        x = [x, x1(p1)];
        p1 = p1 + 1;
    else
        x = [x, x2(p2)];
        p2 = p2 + 1;
    end
    i = i + 1;
end
```
