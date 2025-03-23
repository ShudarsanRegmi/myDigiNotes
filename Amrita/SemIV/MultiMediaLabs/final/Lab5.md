



## Experiment - 12

### AIM : To load an image and display the original image, an image with increased brightness, and an image with decreased brightness by modifying the RGB channels using MATLAB.

### Code
```matlab
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert the image to grayscale
gimg = rgb2gray(img);

% Amount to adjust brightness
amount = 50;

% Increase brightness
bright_gimg = gimg + amount;

% Decrease brightness
dark_gimg = gimg - amount;

% Display images
figure(1);
subplot(2,2,1);
imshow(gimg);
title('Original Image');

subplot(2,2,2);
imshow(gimg);
title('Original Grayscale Image');

subplot(2,2,3);
imshow(bright_gimg);
title('Bright Image');

subplot(2,2,4);
imshow(dark_gimg);
title('Dark Image');

```

### Output
![image](https://github.com/user-attachments/assets/66f3e28f-e853-4dee-af10-9eb124cdcf65)

### Result
> Brightness of an input image was changed using matlab

---

## Experiment - 13

### AIM : To load an image and display the original image, an image with increased brightness, and an image with decreased brightness by modifying the RGB channels using MATLAB.

### Code
```matlab
% Read the input image
img = imread('./resources/size_spec/pikachu.jpeg');

% Increase the brightness by adding 50 to all channels
brightness_img = img + 50;
% Clip values to stay within the valid range [0, 255]
brightness_img = min(brightness_img, 255);

% Decrease the brightness by subtracting 50 from all channels
dim_img = img - 50;
% Clip values to stay within the valid range [0, 255]
dim_img = max(dim_img, 0);

% Display the images
figure(1);

% Original Image
subplot(2, 2, 1);
imshow(img);
title('Original Image');

% Brightness Increased Image
subplot(2, 2, 3);
imshow(brightness_img);
title('Brightness Increased Image');

% Dimmed Image
subplot(2, 2, 4);
imshow(dim_img);
title('Dimmed Image');

```

### Output
![image](https://github.com/user-attachments/assets/e0013a38-7be9-4d2d-9093-f9de7c7e1613)


### Result
> Brightness of an image was changed by increasing or decreasing pixel values of each of the channels

---


## Experiment - 14

### AIM : To load an image, convert it to grayscale if it's in color, and display the original image, the grayscale image, the image with increased contrast, and the image with decreased contrast using MATLAB.

### Code
```matlab
% Read the input image
img = imread('./resources/size_spec/pikachu.jpeg');

img_gray = rgb2gray(img);

% Display the original and processed images
figure(1);

% Original Image
subplot(2, 2, 1);
imshow(img);
title('Original Image');

% Grayscale Image
subplot(2, 2, 2);
imshow(img_gray);
title('Grayscale Image');

% Increase contrast of the grayscale image
con_increase_img = img_gray * 2;
subplot(2, 2, 3);
imshow(con_increase_img);
title('Contrast Increased Image');

% Decrease contrast of the grayscale image
con_decrease_img = img_gray * 0.2;
subplot(2, 2, 4);
imshow(con_decrease_img);
title('Contrast Decreased Image');
```

### Output
![image](https://github.com/user-attachments/assets/b8296a32-a10c-4ab1-8320-b88635ea5543)

### Result
> Constrast of the input image was modified using matlab

---

## Experiment - 15

### AIM : To load an image, convert it to grayscale if it's in color, and display the original image, the grayscale image, and the negative of the grayscale image by inverting the pixel values using MATLAB.

### Code
```matlab
% Read the input image
img = imread('./resources/size_spec/pikachu.jpeg');

% Convert the image to grayscale
img_gray = rgb2gray(img);

% Create the negative of the grayscale image
img_gray_1 = img_gray;
[r, c] = size(img_gray);

% Invert the pixel values to create the negative image
for i = 1:r
    for j = 1:c
        img_gray_1(i, j) = 255 - img_gray(i, j);
    end
end

% Display the images
figure(1);
subplot(1, 3, 1);
imshow(img);
title("Original Image");

subplot(1, 3, 2);
imshow(img_gray);
title("Grayscale Image");

subplot(1, 3, 3);
imshow(img_gray_1);
title("Negative Grayscale Image");

```

### Output
![image](https://github.com/user-attachments/assets/9d2ce79a-2b41-4e7b-b973-a0755fd4271f)

### Result
> Negative of an Image was produced by converting it to grayscale

---

## Experiment - 16

### AIM : To load an image, invert its color channels to create a negative of the image, save the resulting negative image, and display both the original and the negative images using MATLAB.

### Code
```matlab
% Read the input image
img = imread('./resources/size_spec/pikachu.jpeg');

% Get the size of the image (rows, columns, and color channels)
[r, c, color] = size(img);

% Create an empty matrix for the negative image
img_1 = img;

% Loop through each color channel
for k = 1:color
    % Loop through each pixel of the image
    for i = 1:r
        for j = 1:c
            % Invert the pixel value by subtracting from 255
            img_1(i, j, k) = 255 - img(i, j, k);
        end
    end
end

% Display the images
figure(1);

% Original Image
subplot(1, 2, 1);
imshow(img);
title("Original Image");

% Negative Image
subplot(1, 2, 2);
imshow(img_1);
title("Image Negative");

```

### Output
![image](https://github.com/user-attachments/assets/c2daa108-e6b0-442d-82f8-6f91cdfb0226)

### Result
> Each colo channels were changed to negative to produce the negative of an image using matlab
---

## Experiment - 17

### AIM : To load an image,reverting negative to color image.

### Code
```matlab
% Read the input image
img = imread('./resources/size_spec/pikachu.jpeg');

% Get the size of the image (rows, columns, and color channels)
[r, c, color] = size(img);

% Create a color negative image by inverting each color channel
color_negative_img = img;
for k = 1:color
    for i = 1:r
        for j = 1:c
            % Invert the color channel pixel values (creating the negative)
            color_negative_img(i, j, k) = 255 - img(i, j, k);
        end
    end
end

% Revert the color negative back to the original image
reverted_img = color_negative_img;
for k = 1:color
    for i = 1:r
        for j = 1:c
            % Revert the negative by inverting again (subtract from 255)
            reverted_img(i, j, k) = 255 - color_negative_img(i, j, k);
        end
    end
end

% Display the images
figure(1);

% Color Negative Image
subplot(1, 2, 1);
imshow(color_negative_img);
title("Color Negative Image");

% Reverted Image (original image)
subplot(1, 2, 2);
imshow(reverted_img);
title("Reverted Color Image");

```

### Output
![image](https://github.com/user-attachments/assets/b6caaec2-1583-49d2-8f6a-e7bc9615bf3a)

### Result
> Negative of an image was removed and original color was restored
---


