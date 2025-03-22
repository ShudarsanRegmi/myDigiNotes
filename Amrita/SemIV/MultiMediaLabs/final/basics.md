# Basics of Matlab

---

### **1. Variables & Basic Operations**
```matlab
% Define variables
a = 10;
b = 5;

% Basic Arithmetic Operations
sum = a + b;     % Addition
diff = a - b;    % Subtraction
prod = a * b;    % Multiplication
quot = a / b;    % Division
expVal = a^b;    % Exponentiation

% Display output
disp(['Sum: ', num2str(sum)]);
disp(['Product: ', num2str(prod)]);
```

---

### **2. Vectors & Matrices**
```matlab
% Row vector
rowVec = [1 2 3 4 5];

% Column vector
colVec = [1; 2; 3; 4; 5];

% Matrix
A = [1 2 3; 4 5 6; 7 8 9];

% Element-wise operations
B = A .* 2;      % Multiply each element by 2
C = A + A;       % Element-wise addition

% Transpose
ATranspose = A';

% Accessing elements
elem = A(2,3);   % Element in 2nd row, 3rd column

% Display matrix
disp('Matrix A:');
disp(A);
```

---

### **3. Conditional Statements**
```matlab
x = 10;

if x > 0
    disp('x is positive');
elseif x < 0
    disp('x is negative');
else
    disp('x is zero');
end
```

---

### **4. Loops**
```matlab
% For loop
for i = 1:5
    disp(['Iteration: ', num2str(i)]);
end

% While loop
n = 1;
while n <= 5
    disp(['While Loop Iteration: ', num2str(n)]);
    n = n + 1;
end
```

---

### **5. Functions**
```matlab
function output = squareNumber(x)
    output = x^2;
end

% Calling the function
result = squareNumber(4);
disp(['Square of 4: ', num2str(result)]);
```

---

### **6. Plotting**
```matlab
x = linspace(0, 10, 100); % Generate 100 points between 0 and 10
y = sin(x);               % Compute sine values

figure;                   % Create new figure window
plot(x, y, 'r', 'LineWidth', 2);
xlabel('x-axis');
ylabel('y-axis');
title('Sine Wave');
grid on;
```

---

### **7. Reading & Writing Files**
```matlab
% Save data to a file
data = [1 2 3; 4 5 6; 7 8 9];
save('data.mat', 'data');  % Save in .mat format

% Load data
load('data.mat');

% Write to text file
dlmwrite('data.txt', data, 'delimiter', ' ');

% Read from text file
readData = dlmread('data.txt');
disp('Read Data:');
disp(readData);
```

---

### **8. Working with Images**
```matlab
img = imread('image.jpg');  % Read image
grayImg = rgb2gray(img);    % Convert to grayscale
imshow(grayImg);            % Display image
```

---
