# Interpolation


### Code

```matlab
% Define the size of the chessboard
r = 8;
c = 8;

% Create an 8x8 chessboard pattern
chess = zeros(r, c);
for i = 1:r
    for j = 1:c
        chess(i, j) = mod(i + j, 2);
    end
end

% Define scaling factor
scaleFactor = 50;

% Resize using different interpolation methods
chess_nearest = imresize(chess, scaleFactor, 'nearest'); % Nearest Neighbor
chess_bilinear = imresize(chess, scaleFactor, 'bilinear'); % Bilinear Interpolation
chess_bicubic = imresize(chess, scaleFactor, 'bicubic'); % Bicubic Interpolation

% Display Original and Interpolated Images
figure;

subplot(2,2,1);
imshow(chess, 'InitialMagnification', 'fit'); % Show original chessboard
title('Original 8×8 Chessboard');

subplot(2,2,2);
imshow(chess_nearest);
title('Nearest Neighbor Interpolation');

subplot(2,2,3);
imshow(chess_bilinear);
title('Bilinear Interpolation');

subplot(2,2,4);
imshow(chess_bicubic);
title('Bicubic Interpolation');

```

### Output
![image](https://github.com/user-attachments/assets/6b409bd1-2a99-4376-a781-5ba7a1bebed7)

