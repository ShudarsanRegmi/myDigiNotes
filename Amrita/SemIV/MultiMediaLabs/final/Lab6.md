## Experiment - 18

### AIM : To apply a logarithmic transformation to each color channel of an image, normalize the result, and display both the original color image and the log-transformed image using MATLAB.

### Code
```matlab
% Load the image
img = imread('./resources/size_spec/pikachu.jpeg');  % Always using Pikachu image

% Get the size of the image (rows, columns, and color channels)
[r, c, color] = size(img);

% Initialize the log-transformed image as a 3D array
img_log_2 = zeros(r, c, color);

% Apply log transformation for each color channel
for k = 1:color
    for i = 1:r
        for j = 1:c
            % Apply log transformation to each pixel in the color channel
            img_log_2(i, j, k) = 80 * log(1 + double(img(i, j, k)));
        end
    end
end

% Normalize the image to the [0, 1] range
img_log_2 = mat2gray(img_log_2);

% Display the images
figure(1);

% Original Image
subplot(1, 2, 1);
imshow(img);
title("Original Color Image");

% Log Transformed Image
subplot(1, 2, 2);
imshow(img_log_2);
title("Log Transformed Image");
```

### Output
![image](https://github.com/user-attachments/assets/a79e6661-9998-4e6c-bd43-d333aa5a7579)

### Result
> Log Transformation was applied to an input image for its enhancement

---

## Experiment - 19

### AIM : To convert an image to grayscale (if it's in color), apply a logarithmic transformation to the grayscale image, normalize the result, and display the original, grayscale, and log-transformed grayscale images using MATLAB

### Code
```matlab
% Read the image directly (assuming it's always a color image)
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert the color image to grayscale
gray_img = rgb2gray(img);

% Get the size of the grayscale image
[r, c] = size(gray_img);

% Initialize an output matrix for log transformation
img_log_2 = zeros(r, c);

% Apply log transformation
for i = 1:r
    for j = 1:c
        img_log_2(i, j) = 80 * log(1 + double(gray_img(i, j)));
    end
end

% Normalize the transformed image
img_log_2 = mat2gray(img_log_2);

% Display the original, grayscale, and log-transformed images
figure(1);

subplot(1, 3, 1);
imshow(img);
title("Original Image");

subplot(1, 3, 2);
imshow(gray_img);
title("Grayscale Image");

subplot(1, 3, 3);
imshow(img_log_2);
title("Log Transformed Grayscale Image");

```

### Output
![image](https://github.com/user-attachments/assets/5f231f0c-89b2-4e6a-b67e-1951e5ec3dd1)


### Result
> Log transformation was applied to the gray scale image
---

## Experiment - 20

### AIM : To perform gamma correction on an image by normalizing its pixel values, applying a specified gamma value, and displaying both the original and gamma-corrected images using MATLAB

### Code
```matlab
% Read the image directly (assuming it's always a color image)
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert the image to double for calculations
img = double(img);

% Normalize the image to range [0,1]
img_normalized = img / 255;

% Get image dimensions
[rows, cols, color] = size(img_normalized);

% Define gamma correction parameters
gamma = 2;
c = 500;

% Initialize the output matrix for power-law transformation (gamma correction)
img_power = zeros(rows, cols, color);

% Apply gamma correction (power-law transformation)
for i = 1:rows
    for j = 1:cols
        for k = 1:color
            x = img_normalized(i, j, k);
            img_power(i, j, k) = c * (x ^ gamma);
        end
    end
end

% Display the original and gamma-corrected images
figure(1);

subplot(1, 2, 1);
imshow(uint8(img));  
title('Original Image');

subplot(1, 2, 2);
imshow(uint8(img_power));  
title('Gamma Corrected Image');

```

### Output
![image](https://github.com/user-attachments/assets/1087c964-b72d-440b-942f-fee85e426553)


### Result
> Gamma Correction was performed for the given input image
---

## Experiment - 21

### AIM : To enhance the contrast of an image by applying a linear transformation based on min-max normalization.

### Code
```matlab
% Read the image (assuming it's a grayscale or color image)
r = imread('./resources/size_spec/pikachu.jpeg');

% Convert image to double for calculations
r_double = double(r);

% Display the original image
figure(1);
subplot(1, 2, 1);
imshow(r);
title('Original Image');

% Compute the minimum and maximum pixel values
temp_min = min(r_double(:));  % Find the global minimum pixel value
temp_max = max(r_double(:));  % Find the global maximum pixel value

% Compute transformation parameters
m = 255 / (temp_max - temp_min);
c = -m * temp_min;

% Apply contrast stretching transformation
y = m * r_double + c;

% Clip values to the valid range [0, 255] and convert back to uint8
y = uint8(max(0, min(255, y)));

% Display the contrast-stretched image
subplot(1, 2, 2);
imshow(y);
title('Contrast Stretched Image');

```

### Output
![image](https://github.com/user-attachments/assets/a4b2133e-13d1-4dec-86d1-d05ee2cd2e77)

### Result
> Contrast Stretching was performed for the given input image
---

## Experiment - 22 

### AIM : To implement and analyze different image enhancement techniques: image negative, log transformation, power-law transformation, and contrast stretching

### Code
```matlab
% AIM: Implement and analyze different image enhancement techniques:
% Image Negative, Log Transformation, Power-Law Transformation, and Contrast Stretching.

% Read the image (assuming it's always a color image)
img = imread('./resources/size_spec/pikachu.jpeg');

% Display menu for user input
k = input("Choose an image enhancement technique:\n" + ...
          "1. Image Negative\n" + ...
          "2. Log Transformation\n" + ...
          "3. Power-Law Transformation\n" + ...
          "4. Contrast Stretching\n" + ...
          "Enter your choice: ");

% Perform the selected image enhancement technique
if k == 1
    % IMAGE NEGATIVE TRANSFORMATION
    [r, c, color] = size(img);
    img_negative = 255 - img;  % Directly compute negative without loop
    
    % Display results
    figure;
    subplot(1, 2, 1);
    imshow(img);
    title("Original Image");

    subplot(1, 2, 2);
    imshow(img_negative);
    title("Image Negative");

elseif k == 2
    % LOG TRANSFORMATION
    img_double = double(img);  % Convert image to double for calculations
    img_log = 80 * log(1 + img_double);  % Apply log transformation
    img_log = mat2gray(img_log);  % Normalize values
    
    % Display results
    figure;
    subplot(1, 2, 1);
    imshow(img);
    title("Original Image");

    subplot(1, 2, 2);
    imshow(img_log);
    title("Log Transformed Image");

elseif k == 3
    % POWER-LAW (GAMMA) TRANSFORMATION
    img_double = double(img);  % Convert image to double
    img_normalized = img_double / 255;  % Normalize to range [0,1]
    
    gamma = 2;
    c = 500;
    
    img_power = c * (img_normalized .^ gamma);  % Element-wise power
    
    % Clip values to the range [0, 255]
    img_power = uint8(max(0, min(255, img_power)));

    % Display results
    figure;
    subplot(1, 2, 1);
    imshow(img);
    title('Original Image');

    subplot(1, 2, 2);
    imshow(img_power);
    title('Gamma Corrected Image');

elseif k == 4
    % CONTRAST STRETCHING
    img_double = double(img);  % Convert to double
    min_val = min(img_double(:));  % Find the minimum pixel value
    max_val = max(img_double(:));  % Find the maximum pixel value

    % Compute transformation parameters
    m = 255 / (max_val - min_val);
    c = -m * min_val;

    % Apply contrast stretching
    img_contrast = m * img_double + c;

    % Clip values to the valid range [0, 255]
    img_contrast = uint8(max(0, min(255, img_contrast)));

    % Display results
    figure;
    subplot(1, 2, 1);
    imshow(img);
    title("Original Image");

    subplot(1, 2, 2);
    imshow(img_contrast);
    title("Contrast Stretched Image");

else
    % INVALID CHOICE
    msgbox("Invalid choice. Please enter a valid option (1-4).", "Error", "error");
end

```

### Output
![image](https://github.com/user-attachments/assets/82423260-84ba-436c-9977-b0f89e7e14d6)

### Result
> A program was made to do different kinds of transformations based on user input
---



