## Experiment - 8

### AIM : Batch Processing of images to convert them to gray scale and store them in separate directory

### Code
```matlab
inpf = './resources/birds';

outf = fullfile(inpf, 'gray_images');

% create the folder if it doesn't exist
if ~exist(outf, 'dir')
    mkdir(outf)
end

% Get all the images of that folder
imageFiles = dir(fullfile(inpf, '*.jpg'))

% Loop through all the images in the folder

for i = 1:length(imageFiles)
    inputFile = fullfile(inpf, imageFiles(i).name);
    img = rgb2gray(imresize(imread(inputFile), [256, 256]));

    [~, name, ext] = fileparts(imageFiles(i).name);
    outputFileName = fullfile(outf, [name '_gray' ext]);

    % save gray scale image in the new 'gray_images' folder
    imwrite(img, outputFileName);
end

disp('Gray scale images were saved successfully');
```

### Output
![image](https://github.com/user-attachments/assets/f12977c2-5387-4ab4-af2b-b97360c85124)

### Result
> Images were loaded in batch and converterd them in grayscale and were stored in separate folder

---

## Experiment - 9

### AIM : Batch Processing of images to separate their RGB Channels and storing each channels in different folders

### Code
```matlab
inpf = './resources/birds/';
outf = fullfile(inpf, 'color_channels');

if ~exist("outf", 'dir')
    mkdir(outf)
end

imageFiles = dir(fullfile(inpf, '*.jpg'));

% Loop through all the files
for i = 1:length(imageFiles)
    % Get the full path of the current image
    inputFile = fullfile(inpf, imageFiles(i).name);

    % Read the image
    img = imresize(imread(inputFile), [256, 256]);

    % Set Blue and Green Channels to get 
    R = img;
    R(:, :, [2,3]) = 0;

    G = img;
    G(:, :, [1,3]) = 0;

    B = img;
    B(:, :, [1,2]) = 0;

    [~, name, ~] = fileparts(imageFiles(i).name);

    imwrite(R, fullfile(outf, [name '_R.jpg']));
    imwrite(G, fullfile(outf, [name, '_G.jpg']));
    imwrite(B, fullfile(outf, [name, '_B.jpg']));

    % Convert to gray scale using rgb channels
    gray = 0.2989 * double(R) + 0.5870 * double(G) + 0.1140 * double(B);
    gray = uint8(gray);

    imwrite(gray, fullfile(outf, [name, '_gray.jpg']));
end
disp('Color channel and grayscale images have been saved in the "color_channels" folder.');
```

### Output
![image](https://github.com/user-attachments/assets/add83678-98ef-4174-bb4e-307d28d98550)


### Result
> RGB Components of images were separated in batch and stored them separately in different folders
