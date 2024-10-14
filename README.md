# Power Transformation and Rescaling

This repository contains a Python implementation of power transformation and rescaling of images using OpenCV, NumPy, and Matplotlib.

## Description

The code performs power transformations on grayscale images to enhance their contrast and visual clarity. Power transformation is a nonlinear technique widely used in image processing to modify pixel values according to a specified gamma value. By adjusting these values, it can significantly improve the visibility of features in low-contrast images.

### How It Works

1. **Image Reading**:
   - The code reads grayscale images from specified file paths using OpenCV. Two images are processed: one is a medical image and the other is a city image.

2. **Power Transformation**:
   - The function `power_transformation(r, c, gamma)` takes three parameters: the input image (`r`), a constant factor (`c`), and the gamma value (`gamma`). The transformation is applied using the formula:
     \[
     s = c \cdot r^{\text{gamma}}
     \]
   - This transformation modifies the pixel intensity values based on the specified gamma, enhancing certain features of the image.

3. **Rescaling**:
   - The `rescale(img)` function normalizes the pixel values of the transformed image to the range of 0 to 255. This is crucial for displaying the images correctly.

4. **Image Display**:
   - The transformed images are stacked horizontally and vertically using NumPy to create a composite image for better visualization. The final result is displayed using Matplotlib.

### Code Breakdown

- **Input Images**:
  - The medical image is read from the `mr_img_path`, and the city image is read from the `city_img_path`.
  
- **Gamma Values**:
  - For the medical image, three gamma values (0.6, 0.4, 0.3) are applied to demonstrate the effects of power transformation.
  - For the city image, three different gamma values (3, 4, 5) are applied to observe the contrast enhancement.

- **Output Visualization**:
  - The processed images are combined into a single output, allowing for a side-by-side comparison of the original and transformed images.

### Usage

1. Place your images in the `images` directory.
2. Modify the `mr_img_path` and `city_img_path` variables in the code to point to your images.
3. Run the script to see the power transformation effects on the images.

### Dependencies

- numpy
- opencv-python
- matplotlib

### Example Images

#### City Image Results

The following output shows the original city image alongside the transformed images with different gamma values:

### Original Image 
![sehir_img](https://github.com/user-attachments/assets/9efe743d-db24-48ae-a2ce-d9857d5baa00)

### Result Image
![sehir](https://github.com/user-attachments/assets/3f2fc130-453b-47c3-a41e-24ec674bfcc3)


