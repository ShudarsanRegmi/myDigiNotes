
## Upsampling and Downsampling

```matlab
% Define the file path
ffp = 'C:\Users\STUDENT\Desktop\Shud\pandas.jpg';
img = imread(ffp);

% Create a figure for displaying the images
figure(1);

% Original Image
subplot(2, 2, 1);
imshow(img);
title('Original Image');

% Convert the image to grayscale
img_gray = rgb2gray(img);
subplot(2, 2, 2);
imshow(img_gray);
title('Grayscale Image');

% Downsampling the image
sf = 10;  % Scaling factor for downsampling
img_dg = img_gray(1:sf:end, 1:sf:end);
subplot(2, 2, 3);
imshow(img_dg);
title('Downsampled Image (sf = 10)');

% Upscaling the downsampled image
img_up = imresize(img_gray, [size(img_gray, 1) * 1.2, size(img_gray, 2) * 1.2], 'nearest');
subplot(2, 2, 4);
imshow(img_up);
title('Upscaled Image (1.2x)');
```

### Output
![image](https://github.com/user-attachments/assets/0fc9631a-ad96-437d-833d-074ac154b0fb)


## Changing the Brightness of an Image


```matlab
% Increasing and decreasing brightness

ffp = 'C:\Users\STUDENT\Desktop\Shud\pandas.jpg';  % Path to the image
img = imread(ffp);  % Read the image

img_gray = rgb2gray(img);  % Convert the image to grayscale

% Brighten the image by adding 100 to each pixel intensity
brt_img = img_gray + 100;

% Dim the image by subtracting 100 from each pixel intensity
dim_img = img_gray - 100;

figure(1);

% Display the original grayscale image with a meaningful title
subplot(1,3,1);
imshow(img_gray);
title('Original Grayscale Image');  % Title for the first subplot

% Display the brightened image with a meaningful title
subplot(1,3,2);
imshow(brt_img);
title('Brightened Image (+100)');  % Title for the second subplot

% Display the dimmed image with a meaningful title
subplot(1,3,3);
imshow(dim_img);
title('Dimmed Image (-100)');  % Title for the third subplot

```

### Output
![image](https://github.com/user-attachments/assets/5463b0e9-a33d-47ac-b3d2-43e0d0500833)


## Changing the constrast 

```matlab
% Changing the Contrast

% Define the file path to the image
ffp = 'C:\Users\STUDENT\Desktop\Shud\pandas.jpg';  % Path to the image
img = imread(ffp);  % Read the image

% Convert the image to grayscale
img_gray = rgb2gray(img);  % Convert the color image to grayscale

% Create a figure for displaying the images
figure(1);

% Increase the contrast by multiplying the image by 1.5
img1 = img_gray * 1.5;  % Multiply each pixel by 1.5, making the light areas lighter and dark areas darker.

% Decrease the contrast by multiplying the image by 0.5
img2 = img_gray * 0.5;  % Multiply each pixel by 0.5, reducing the difference between light and dark areas.

% Display the original grayscale image with a meaningful title
subplot(2,2,1);
imshow(img_gray);
title('Original Grayscale Image');  % Title for the first subplot

% Display the high-contrast image with a meaningful title
subplot(2,2,2);
imshow(img1);
title('Increased Contrast (×1.5)');  % Title for the second subplot

% Display the low-contrast image with a meaningful title
subplot(2,2,3);
imshow(img2);
title('Decreased Contrast (×0.5)');  % Title for the third subplot
```

### Output
![image](https://github.com/user-attachments/assets/cb65ca9c-0360-41a1-8dc0-9697888fae71)




