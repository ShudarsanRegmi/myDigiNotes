## Image Structure in Matlab

![image](https://github.com/user-attachments/assets/00868019-c75a-4b29-adbd-1ae2b92a7a07)


### Creating a binary image 

```matlab
% Define a 10×10 binary image manually (values 0 and 1)
binaryImg = [ 1 0 1 0 1 0 1 0 1 0;
              0 1 0 1 0 1 0 1 0 1;
              1 1 0 0 1 1 0 0 1 1;
              0 0 1 1 0 0 1 1 0 0;
              1 0 1 0 1 0 1 0 1 0;
              0 1 0 1 0 1 0 1 0 1;
              1 1 0 0 1 1 0 0 1 1;
              0 0 1 1 0 0 1 1 0 0;
              1 0 1 0 1 0 1 0 1 0;
              0 1 0 1 0 1 0 1 0 1];

% Convert to uint8 format (0 → Black, 255 → White)
binaryImg = uint8(binaryImg * 255);

% Display size
disp('Binary Image Size:');
disp(size(binaryImg));  % Output: [10 10]

% Display numerical pixel values
disp('Binary Image Pixel Values:');
disp(binaryImg);

% Show the binary image
figure;
imshow(binaryImg);
title('10×10 Binary Image');

```

#### Output
![image](https://github.com/user-attachments/assets/220a5efb-bab6-4d4d-a42a-a8b1c3463b20)

### Creating a color image by using numerical values

**Simple image** <br>

```matlab
r = [1,1,1,0,0,0 0,0,0];
g = [0,0,0,1,1,1,0,0,0];
b = [0,0,0,0,0,0,1,1,1];


im = cat(3, r,g,b);


imshow(imresize(im,40,"nearest")); % Interpolation
```
**Output** <br>

![image](https://github.com/user-attachments/assets/5941c3f3-ba67-4de5-b07a-26797ca98280)


```matlab
% Define a 5×5 RGB image
img = cat(3, ...
    [255 128   0  75 200; 100  50  25 150  80;  60  90 120 180  30; 210 170  40 130 220;  10 250 140  55 190], ...  % Red
    [  0 255  50 100  25; 200  25 128  75 150;  90 140  30 160 180;  40 110 220 190 250; 255  80  60  10 230], ...  % Green
    [ 50 100 255   0 200; 180 200  25 255 128;  75 220 150  40  90; 160  30 250 120  10; 128 255  80 210  60]);     % Blue

% Display size
disp('Image Size:');
disp(size(img)); % Output: [5 5 3]

% Show Red, Green, and Blue channels separately
disp('Red Channel:'); disp(img(:,:,1));
disp('Green Channel:'); disp(img(:,:,2));
disp('Blue Channel:'); disp(img(:,:,3));

% Convert to grayscale
grayImg = rgb2gray(uint8(img));
disp('Grayscale Image:'); disp(grayImg);

% Display the image and its channels correctly
figure;

% Original RGB Image
subplot(2,2,1);
imshow(uint8(img));
title('Original RGB Image');

% Red Channel (Retaining 3D format but setting G and B to zero)
redOnly = img; redOnly(:,:,2) = 0; redOnly(:,:,3) = 0;
subplot(2,2,2);
imshow(uint8(redOnly));
title('Red Channel');

% Green Channel (Setting R and B to zero)
greenOnly = img; greenOnly(:,:,1) = 0; greenOnly(:,:,3) = 0;
subplot(2,2,3);
imshow(uint8(greenOnly));
title('Green Channel');

% Blue Channel (Setting R and G to zero)
blueOnly = img; blueOnly(:,:,1) = 0; blueOnly(:,:,2) = 0;
subplot(2,2,4);
imshow(uint8(blueOnly));
title('Blue Channel');
```
#### Output

![image](https://github.com/user-attachments/assets/6cfb570d-b3d0-4249-ac8f-6036bfe8a945)

---

## **1️⃣ Understanding the Image as a 3D Matrix**
The given **5×5 RGB image** is stored as a **5×5×3 matrix**, where:
- **Dimension 1 (Rows)**: Controls the vertical position (top to bottom).
- **Dimension 2 (Columns)**: Controls the horizontal position (left to right).
- **Dimension 3 (Channels)**: Controls the color (Red, Green, Blue).

#### **Matrix Structure:**
Each pixel is represented as a **(R, G, B) triplet**, meaning for a pixel at **row i, column j**, the values are stored in:
```plaintext
img(i, j, 1)  -> Red
img(i, j, 2)  -> Green
img(i, j, 3)  -> Blue
```
For example, the pixel at position **(2,3)** (2nd row, 3rd column) has:
```matlab
Red   = img(2,3,1) = 25
Green = img(2,3,2) = 128
Blue  = img(2,3,3) = 25
```
So the pixel **(2,3) has RGB = (25, 128, 25)**.

---

## **2️⃣ Full Numerical Breakdown**
Let's look at the **full 5×5 matrix** for each channel:

### **Red Channel (img(:,:,1))**
```plaintext
 255   128     0    75   200
 100    50    25   150    80
  60    90   120   180    30
 210   170    40   130   220
  10   250   140    55   190
```
🔴 **Represents red intensity** at each pixel.

### **Green Channel (img(:,:,2))**
```plaintext
   0   255    50   100    25
 200    25   128    75   150
  90   140    30   160   180
  40   110   220   190   250
 255    80    60    10   230
```
🟢 **Represents green intensity** at each pixel.

### **Blue Channel (img(:,:,3))**
```plaintext
  50   100   255     0   200
 180   200    25   255   128
  75   220   150    40    90
 160    30   250   120    10
 128   255    80   210    60
```
🔵 **Represents blue intensity** at each pixel.

---

## **3️⃣ Mapping a Few Pixels Numerically**
### **Pixel at (1,1) → Top-left Corner**
- **R = img(1,1,1) = 255** → High red intensity (bright red)
- **G = img(1,1,2) = 0** → No green
- **B = img(1,1,3) = 50** → Some blue
- **Final RGB**: **(255, 0, 50) → Reddish with a bit of blue**

### **Pixel at (3,4) → Middle of Image**
- **R = img(3,4,1) = 180** → Strong red
- **G = img(3,4,2) = 160** → Moderate green
- **B = img(3,4,3) = 40** → Weak blue
- **Final RGB**: **(180, 160, 40) → Yellowish-brown**

### **Pixel at (5,5) → Bottom-right Corner**
- **R = img(5,5,1) = 190**
- **G = img(5,5,2) = 230**
- **B = img(5,5,3) = 60**
- **Final RGB**: **(190, 230, 60) → Light Greenish-Yellow**

---

## **4️⃣ MATLAB Representation of Structure**
```matlab
% Access pixel at row=3, column=4
pixel = img(3,4,:); % Extract RGB values
disp(['RGB at (3,4): ', num2str(pixel(:)')]); 
```
**Output:**
```plaintext
RGB at (3,4): 180 160 40
```

---

## **5️⃣ Visualizing the Image with Pixel Numbers**
Here’s a **conceptual way to see the image with numerical intensities**:

```
(255,  0,  50)  (128, 255, 100)  (  0,  50, 255)  ( 75, 100,  0)  (200,  25, 200)
(100,200,180)  ( 50,  25,200)  ( 25,128, 25)  (150,  75,255)  ( 80,150,128)
( 60, 90, 75)  ( 90,140,220)  (120, 30,150)  (180,160, 40)  ( 30,180, 90)
(210, 40,160)  (170,110, 30)  ( 40,220,250)  (130,190,120)  (220,250, 10)
( 10,255,128)  (250, 80,255)  (140, 60, 80)  ( 55, 10,210)  (190,230, 60)
```
Each tuple `(R, G, B)` represents a pixel!

---

## **Final Takeaways**
1. **Stored as a 3D matrix** → **(Height × Width × 3)**
2. **Each pixel has 3 numbers (R, G, B)** stored in separate layers.
3. **Accessing a pixel's RGB**: `img(i, j, :)`
4. **Flattened as**:
   ```matlab
   reshapedImg = reshape(img, [], 3);
   ```
   - Converts the **5×5×3 matrix** into a **25×3 matrix** (useful for ML).

---

