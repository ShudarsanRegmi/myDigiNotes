## Experiment - 10

### AIM : To convert an image to grayscale, then downscale it by a factor, and display the original, grayscale, and downscaled images using MATLAB.

### Code
```matlab
clc; close all; clear all;
img = imread('./resources/size_spec/pikachu.jpeg');

sf = 7;

dsimg = img(1:sf:end, 1:sf:end, :);

gimg = rgb2gray(img);
dsgimg = gimg(1:sf:end, 1:sf:end);

figure(1);
subplot(2,2,1);
imshow(img);
title('Original Image');

subplot(2,2,2);
imshow(dsimg);
title('Downsampled Original Image');

subplot(2,2,3);
imshow(gimg);
title('Gray image');

subplot(2,2,4);
imshow(dsgimg);
title('Downsampled Grayscale Image');
```

### Output
![image](https://github.com/user-attachments/assets/68c8a468-a7e0-4fb1-818f-0bd4b41cb55b)

### Result
> The input image was downsampled by the given scale factor

---

## Experiment - 11

### AIM : To convert an image to grayscale, downscale it by a factor of 4, upscale it to a fixed size of 512x512 using nearest-neighbor interpolation, and display the original, grayscale, downscaled, and upscaled images using MATLAB.

### Code 
```matlab
clc; close all; clear all;
img = imread('./resources/size_spec/pikachu.jpeg');
imggray=rgb2gray(img);;

% down sampling
sf=4;
img_dg=imggray(1:sf:end,1:sf:end);

% upsampling
img_up = imresize(imggray, [512, 512], 'nearest');

figure(1);
subplot(1,4,1)
imshow(img)
title("original image");

subplot(1,4,2)
imshow(imggray)
title("gray image");

subplot(1,4,3)
imshow(img_dg)
title("Downsampled image");
subplot(1,4,4);
imshow(img_up);
title("Upsampled image");
```

### Output
![image](https://github.com/user-attachments/assets/e3041d72-37fc-4b26-b06d-a8b7f1eec6de)



### Result
> The images were successfully upsampled and downsampled by the given parameters
