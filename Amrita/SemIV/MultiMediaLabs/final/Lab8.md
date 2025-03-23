## Experiment - 25

### AIM : To analyze the histogram of images with different brightness and contrast levels

### Code
```matlab
% Load images using correct paths
x = imread("./resources/histogram/darkgray.jpg");
y = imread("./resources/histogram/brightgray.jpg");
z = imread("./resources/histogram/lowcontrast.ppm");
a = imread("./resources/histogram/highcontrast.jpg");

% Create figure and display images with histograms
figure(1)

% Dark Gray Image
subplot(4,2,1);
imshow(x);
title('Dark Gray Image');

subplot(4,2,2);
imhist(x, 64);
title('Histogram of Dark Gray');

% Bright Gray Image
subplot(4,2,3);
imshow(y);
title('Bright Gray Image');

subplot(4,2,4);
imhist(y, 64);
title('Histogram of Bright Gray');

% Low Contrast Image
subplot(4,2,5);
imshow(z);
title('Low Contrast Image');

subplot(4,2,6);
imhist(z, 64);
title('Histogram of Low Contrast');

% High Contrast Image
subplot(4,2,7);
imshow(a);
title('High Contrast Image');

subplot(4,2,8);
imhist(a, 64);
title('Histogram of High Contrast');

```

### Output
![image](https://github.com/user-attachments/assets/92013d47-b63b-4f77-aaa5-af30a9fc8af2)

### Result
> Histogram of Images of different characteristics were analyzed
--- 

## Experiment - 26

### AIM : To enhance the contrast of grayscale images using histogram equalization and compare the results

### Code
```matlab
% Load images using correct filenames and paths
x = imread("./resources/histogram/darkgray.jpg");
y = imread("./resources/histogram/brightgray.jpg");
z = imread("./resources/histogram/lowcontrast.ppm");
a = imread("./resources/histogram/highcontrast.jpg");

figure(1)

% Dark Gray Image
subplot(4,2,1);
imshow(x);
title('Original Dark Gray');

subplot(4,2,2);
x_eq = histeq(x);
imshow(x_eq);
title('Equalized Dark Gray');

% Bright Gray Image
subplot(4,2,3);
imshow(y);
title('Original Bright Gray');

subplot(4,2,4);
y_eq = histeq(y);
imshow(y_eq);
title('Equalized Bright Gray');

% Low Contrast Image
subplot(4,2,5);
imshow(z);
title('Original Low Contrast');

subplot(4,2,6);
z_eq = histeq(z);
imshow(z_eq);
title('Equalized Low Contrast');

% High Contrast Image
subplot(4,2,7);
imshow(a);
title('Original High Contrast');

subplot(4,2,8);
a_eq = histeq(a);
imshow(a_eq);
title('Equalized High Contrast');

```

### Output
![image](https://github.com/user-attachments/assets/bbc1a739-297a-41cd-8d77-f60561ac2682)

### Result
> Histogram Equalization was applied to images of different characteristics
--- 

## Experiment - 27

### AIM : To perform histogram matching on an image using a reference grayscale image and analyze the results

### Code
```matlab
A = imread('./resources/histogram/img1.bmp');
Ref = imread('./resources/histogram/darkgray.jpg'); % Using darkgray.jpg as reference

% Convert to grayscale
A_gray = rgb2gray(A);
Ref_gray = rgb2gray(Ref);

% Apply histogram matching
B_gray = imhistmatch(A_gray, Ref_gray);

% Display results
figure(1)

subplot(3,2,1);
imshow(A_gray);
title('Original Image (Grayscale)');

subplot(3,2,2);
imhist(A_gray, 64);
title('Histogram of Original');

subplot(3,2,3);
imshow(Ref_gray);
title('Reference Image (Grayscale)');

subplot(3,2,4);
imhist(Ref_gray, 64);
title('Histogram of Reference');

subplot(3,2,5);
imshow(B_gray);
title('Histogram Matched Image');

subplot(3,2,6);
imhist(B_gray, 64);
title('Histogram of Matched Image');

```

### Output
![image](https://github.com/user-attachments/assets/b0982586-6e6b-4f81-ae75-4ff83018cc6a)

### Result
> Histogram matching was applied to an input image based on a given reference image using matlab
--- 

## Experiment - 28

### AIM : To perform histogram matching on an RGB image using a reference image where only the green channel is preserved

### Code
```matlab
% Read the input image (Pikachu)
A = imread('./resources/histogram/pikachu.jpg');

% Read the reference image (Bright Gray)
x = imread('./resources/histogram/brightgray.jpg');

% Extract the green channel only
Ref = x;
Ref(:,:,1) = 0; % Set Red channel to 0
Ref(:,:,3) = 0; % Set Blue channel to 0

% Convert the reference to grayscale (since only green remains)
Ref_gray = Ref(:,:,2);

% Apply histogram matching only on the green channel
A_red = A(:,:,1);  % Red channel remains unchanged
A_green = imhistmatch(A(:,:,2), Ref_gray); % Green channel matched
A_blue = A(:,:,3);  % Blue channel remains unchanged

% Reconstruct the final image with adjusted green channel
B = cat(3, A_red, A_green, A_blue);

% Display results
figure(1)

subplot(3,2,1);
imshow(A);
title('Original Pikachu Image');

subplot(3,2,2);
imhist(A(:,:,2), 64);
title('Histogram of Pikachu (Green)');

subplot(3,2,3);
imshow(Ref);
title('Reference Image (Bright Gray - Green Only)');

subplot(3,2,4);
imhist(Ref_gray, 64);
title('Histogram of Reference (Green)');

subplot(3,2,5);
imshow(B);
title('Histogram Matched Pikachu');

subplot(3,2,6);
imhist(B(:,:,2), 64);
title('Histogram of Matched Pikachu (Green)');

```

### Output
![image](https://github.com/user-attachments/assets/4778602d-df2a-4cff-8033-0344adc2681c)


### Result
> Histogram matching was performed by preservig only the green channel
--- 
