## Experiment - 23

### AIM : To perform gray-level slicing on a grayscale image and visualize the effect of different slicing levels

### Code
```matlab
% Read the Pikachu image (assuming it's grayscale or converting it to grayscale)
img = rgb2gray(imread('./resources/size_spec/pikachu.jpeg'));

% Display original grayscale image
figure;
subplot(2,2,1);
imshow(img);
title('Original Grayscale Pikachu');

% Apply gray-level slicing at different levels
slice_256 = img > 256 / 2;  % Threshold at 128
slice_128 = img > 128;      % Threshold at 128
slice_64  = img > 64;       % Threshold at 64

% Display sliced images
subplot(2,2,2);
imshow(slice_256);
title('Gray Slice at 256 Levels');

subplot(2,2,3);
imshow(slice_128);
title('Gray Slice at 128 Levels');

subplot(2,2,4);
imshow(slice_64);
title('Gray Slice at 64 Levels');

```

### Output
![image](https://github.com/user-attachments/assets/05aa62a6-8307-42b2-8247-68edb6278143)

### Code
```matlab
% Read the Pikachu image
img = rgb2gray(imread('./resources/size_spec/pikachu.jpeg'));

% Display original grayscale image
figure;
subplot(2,2,1);
imshow(img);
title('Original Grayscale Pikachu');

% Apply gray-level slicing using grayslice
slice_256 = grayslice(img, 256);
slice_128 = grayslice(img, 128);
slice_64  = grayslice(img, 64);

% Display sliced images
subplot(2,2,2);
imshow(slice_256);
title('Gray Slice at 256 Levels');

subplot(2,2,3);
imshow(slice_128);
title('Gray Slice at 128 Levels');

subplot(2,2,4);
imshow(slice_64);
title('Gray Slice at 64 Levels');

```
### Output

![image](https://github.com/user-attachments/assets/043f737f-7e45-494e-be23-d93a37b1d0d1)

### Result
> Gray level slicing was performed for the given input image
--- 

## Experiment - 24

### AIM : To perform bit-plane slicing on a grayscale image and visualize individual bit planes

### Code
```matlab
% Read the Pikachu image
a = imread('./resources/size_spec/pikachu.jpeg');

% Convert to grayscale if it's a color image
a = rgb2gray(a);

% Get image size
[m, n] = size(a);

% Convert image to double for processing
b = double(a);

% Convert each pixel to an 8-bit binary representation
c = de2bi(b(:), 8, 'left-msb'); 

% Extract bit planes
r1 = reshape(c(:,1), [m, n]);
r2 = reshape(c(:,2), [m, n]);
r3 = reshape(c(:,3), [m, n]);
r4 = reshape(c(:,4), [m, n]);
r5 = reshape(c(:,5), [m, n]);
r6 = reshape(c(:,6), [m, n]);
r7 = reshape(c(:,7), [m, n]);
r8 = reshape(c(:,8), [m, n]);

% Display images
figure;
subplot(2, 5, 1);
imshow(a);
title('Original Pikachu');

subplot(2, 5, 2);
imshow(logical(r1));
title('Bit Plane 1');

subplot(2, 5, 3);
imshow(logical(r2));
title('Bit Plane 2');

subplot(2, 5, 4);
imshow(logical(r3));
title('Bit Plane 3');

subplot(2, 5, 5);
imshow(logical(r4));
title('Bit Plane 4');

subplot(2, 5, 6);
imshow(logical(r5));
title('Bit Plane 5');

subplot(2, 5, 7);
imshow(logical(r6));
title('Bit Plane 6');

subplot(2, 5, 8);
imshow(logical(r7));
title('Bit Plane 7');

subplot(2, 5, 9);
imshow(logical(r8));
title('Bit Plane 8');

```

### Output

### Result
> Differetnt bit planes of an image was visualized using matlab
