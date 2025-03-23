## Experiment - 29

### AIM : To apply Laplacian filtering using 4-neighbour and 8-neighbour kernels for edge detection and image enhancement

### Code
```matlab
% Read the input image (Pikachu)
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert to grayscale
gray = rgb2gray(img);

% Define the 8-neighbor Laplacian kernel
h1 = [1,1,1; 1,-8,1; 1,1,1];

% Convolution with the 8-neighbor kernel
res1 = conv2(double(gray), h1, 'same');

% Define the 4-neighbor Laplacian kernel
h = [0,1,0; 1,-4,1; 0,1,0];

% Convolution with the 4-neighbor kernel
res = conv2(double(gray), h, 'same');

% Display the results
figure(1)

subplot(1,3,1);
imshow(gray);
title('Original Image');

subplot(1,3,2);
imshow(uint8(abs(res))); % Convert back to uint8 for display
title('Processed Image (4-Neighbor)');

subplot(1,3,3);
imshow(uint8(abs(res1))); % Convert back to uint8 for display
title('Processed Image (8-Neighbor)');

```

### Output
![image](https://github.com/user-attachments/assets/021faf82-36d2-4848-a49c-52b9a5632404)


### Result
> Laplacian filtering was applied by using 4-neighbor and 8-neighbor
--- 

## Experiment - 30

### AIM : To apply spatial filtering techniques for image smoothing using box averaging and weighted filtering

### Code
```matlab
% Read the input image (Pikachu)
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert to grayscale
gray = rgb2gray(img);

% Define the 3x3 Box Filter (Uniform Averaging)
h = 1/9 * [1,1,1; 1,1,1; 1,1,1];

% Define the 5x5 Weighted Filter
h1 = 1/80 * [2,2,2,2,2; 2,4,6,4,2; 2,6,8,6,2; 2,4,6,4,2; 2,2,2,2,2];

% Apply convolution with both filters
res = conv2(double(gray), h, 'same');
res1 = conv2(double(gray), h1, 'same');

% Display results
figure(1)

subplot(1,3,1);
imshow(gray);
title("Original Image");

subplot(1,3,2);
imshow(uint8(res));
title("Processed for Box Average Image");

subplot(1,3,3);
imshow(uint8(res1));
title("Processed for Weighted 5×5 Image");

```

### Output
![image](https://github.com/user-attachments/assets/0e572ef3-c8b3-4c3d-b80a-f714ae5480c7)

### Result

--- 

## Experiment - 31

### AIM : To perform morphological operations (dilation, erosion, opening, and closing) on a binary image using a diamond-shaped structuring element

### Code
```matlab
% Create a binary image
BW = zeros(9,10);
BW(4:6,4:7) = 1;

% Display the original binary image
figure(1)
subplot(1,5,1);
imshow(imresize(BW, 40, "nearest"));
title('Original Image');

% Create structuring elements
SE = strel('diamond',3); % Diamond-shaped SE for dilation
SE1 = strel('diamond',1); % Diamond-shaped SE for erosion

% Apply Dilation
BW2 = imdilate(BW, SE);
subplot(1,5,2);
imshow(imresize(BW2, 40, "nearest"));
title("Dilated Image");

% Apply Erosion
BW3 = imerode(BW, SE1);
subplot(1,5,3);
imshow(imresize(BW3, 40, "nearest"));
title("Eroded Image");

% Apply Opening (Erosion followed by Dilation)
BW4 = imdilate(BW3, SE1);
subplot(1,5,4);
imshow(imresize(BW4, 40, "nearest"));
title("Opening Image");

% Apply Closing (Dilation followed by Erosion)
BW5 = imerode(BW2, SE);
subplot(1,5,5);
imshow(imresize(BW5, 40, "nearest"));
title("Closed Image");

```

### Output
![image](https://github.com/user-attachments/assets/1b04625f-e09d-4ffc-946a-b1935cef9449)

### Result
> Morphological Operations was applied to an image
