

## Experiment - 4

### AIM : Detection of Color or Grayscale Image with Message Display in MATLAB

### Code
```matlab
clc;close all;clear all;
img = imread('./resources/size_spec/pikachu.jpeg');
if size(img,3) == 3
    msgbox('color image')
else
    msgbox('grayscale image')
end
```

### Output
![image](https://github.com/user-attachments/assets/26f4a1f1-5687-41ba-ba78-9631d1c0007b)


### Result
> Image was successfully classified as color or grayscale image

--- 



## Experiment - 5

### AIM : Extract RGB Channels from a color image

### Code
```matlab
% Read the image
img = imread('peppers.png');

% Extract the Red, Green, and Blue channels
R = img(:,:,1);  % Red channel
G = img(:,:,2);  % Green channel
B = img(:,:,3);  % Blue channel

% Display the individual channels
subplot(1, 4, 1), imshow(img), title('Original Image');
subplot(1, 4, 2), imshow(R), title('Red Channel');
subplot(1, 4, 3), imshow(G), title('Green Channel');
subplot(1, 4, 4), imshow(B), title('Blue Channel');
```

### Output
![image](https://github.com/user-attachments/assets/afbab131-57c6-4df6-8a97-a8504c187a27)

### Code
```matlab
clc; close all; clear all;

% Read the image
img = imread('peppers.png');

r = img;
g = img;
b = img;

r(:, :, 2:3) = 0;
g(:, :, [1,3]) = 0;
b(:, :, 1:2) = 0;

figure(1);

subplot(1,4,1);
imshow(img);
title('Original Image');

subplot(1,4,2);
imshow(r);
title('Red Channel');

subplot(1,4,3);
imshow(g);
title('Green Channel');

subplot(1,4,4);
imshow(b);
title('Blue Channel');

```

### Output
![image](https://github.com/user-attachments/assets/b09c4310-fa8e-4e26-9b12-99e67ad98fd0)

### Result
> RGB Chanels from an image was successfully separated and displayed using matlab

## Experiment - 6

### AIM : Concatinating Red, Green and Blue Channels of Images

**For Same Image**
### Code
```matlab

```
### Output
![image](https://github.com/user-attachments/assets/c9227ad8-a8c1-4e7f-b09c-7d1e900b5215)

**For Different Images of same size**
### Code
```matlab
clc; close all; clear all;

% Read the image
img1 = imread('./resources/same_size/img1.jpg');
img2 = imread('./resources/same_size/img2.jpg');
img3 = imread('./resources/same_size/img3.jpg');

r1 = img1(:, :, 1);
g2 = img2(:, :, 2);
b3 = img3(:, :, 3);

figure(1);

subplot(1,3,1);
imshow(img1);
title('Image 1');

subplot(1,3,2);
imshow(img2);
title('Image 2');

subplot(1,3,3);
imshow(img3);
title('Image 3');


figure(2);
% we need to single channel,
imshow(cat(3, r1, g2, b3));
title("Channels combined of different image")
```

### Output
![Uploading image.png…]()

### Result




