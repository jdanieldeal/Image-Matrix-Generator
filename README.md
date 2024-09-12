# Image Matrix Generator

## Description

The **Image Matrix Generator** is a Python program that allows users to create a matrix of images arranged in a grid format. You can specify the number of rows and columns, customize the border thickness and color, and select input and output folders for image processing. The program generates a single output image for each batch of images in the input folder, forming a grid-like matrix.

## Features
- Choose the number of rows and columns for the image grid.
- Customize the border thickness and color.
- Automatically generates matrices from images in the input folder.
- Processes all common image formats (.jpg, .jpeg, .png, .gif).
- Simple GUI for easy interaction.

## Prerequisites

- **Python 3.x** installed on your system
- Required libraries:
  - `Pillow`
  - `PyQt5`
  
  You can install them using pip:
  ```bash
  pip install Pillow PyQt5
  ```

## How to Use

1. **Input Folder:** Select the folder containing the images you want to use in the matrix.
2. **Output Folder:** Choose the folder where the generated image matrix will be saved.
3. **Rows and Columns:** Specify the number of rows and columns to arrange the images.
4. **Base Filename:** Set the base name for the output files.
5. **Border Thickness and Color:** Set the thickness and color of the borders between images (optional).
6. **Generate Matrix:** Click "Generate Matrix" to create the image matrix.

### Example

1. Launch the program:
   ```bash
   python image_matrix_generator.py
   ```

2. Follow the steps above in the graphical user interface.

## Notes

- Large matrices may result in very large output images. Adjust the settings to avoid oversized files.
- Ensure that both the input and output folders exist before generating the matrix.

## License

This project is licensed under the MIT License.
