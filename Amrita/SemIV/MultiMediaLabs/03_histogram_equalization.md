# Histogram Equalization


### Darker High Contrast Image

```matlab
% Read the image from the URL
img = imread('https://pbblogassets.s3.amazonaws.com/uploads/2017/09/01110149/tonal-cover.jpg');

% Convert to grayscale if it's a color image
if size(img, 3) == 3
    img = rgb2gray(img);
end

% Apply histogram equalization
imgeq = histeq(img);

% Display original image, histogram, equalized image, and histogram in a single figure
figure;
subplot(2, 2, 1); % First subplot (Original Image)
imshow(img);
title('Original Image');

subplot(2, 2, 2); % Second subplot (Histogram of Original Image)
imhist(img);
title('Histogram of Original Image');

subplot(2, 2, 3); % Third subplot (Equalized Image)
imshow(imgeq);
title('Histogram Equalized Image');

subplot(2, 2, 4); % Fourth subplot (Histogram of Equalized Image)
imhist(imgeq);
title('Histogram of Equalized Image');

```
**I need to paste the output below**




