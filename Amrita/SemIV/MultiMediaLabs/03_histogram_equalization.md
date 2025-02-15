# Histogram Equalization


### Darker High Contrast Image

```matlab
% Read the image from the URL
img = imread('https://pbblogassets.s3.amazonaws.com/uploads/2017/09/01110149/tonal-cover.jpg');

% Convert to grayscale if it's a color image
if size(img, 3) == 3
    img = rgb2gray(img);
end

% Display original image and its histogram
figure(1);
subplot(1,2,1);
imshow(img);
title('Original Image');

subplot(1,2,2);
imhist(img);
title('Histogram of Original Image');

% Apply histogram equalization
imgeq = histeq(img);

% Display equalized image and its histogram
figure(2);
subplot(1,2,1);
imshow(imgeq);
title('Histogram Equalized Image');

subplot(1,2,2);
imhist(imgeq);
title('Histogram of Equalized Image');

```
**I need to paste the output below**

**Input Image**

![{D381CCC5-B686-4E24-8187-7254CBF37956}](https://github.com/user-attachments/assets/8e1078f3-2b72-4f61-a63a-6324d7de944b)

**Output Histogram**
![{C32DB1F3-84E2-42FC-909E-50B2D00E8BFB}](https://github.com/user-attachments/assets/6a22ef72-a42e-4995-a931-00640b1ccec3)


