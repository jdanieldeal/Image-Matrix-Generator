# Image Matrix Generator

## Description

The **Image Matrix Generator** is a Python program that allows users to create a matrix of images arranged in a grid format. You can specify the number of rows and columns, customize the border thickness and color, and select input and output folders for image processing. The program generates a single output image for each batch of images in the input folder, forming a grid-like matrix.

## Why?

I create risograph animations (sort of) and part of the process of creating the animation is putting the frames from a video into a grid, then printing the image of the grid onto a piece of paper. Check my instagram for examples https://www.instagram.com/scanning_matrices/. I used to arrange them into grids by hand in Photoshop and Illustrator and it always took forever. So with what little knowledge I have with coding I knew there would be a way to make a simple program to automate this process and this is how I wrote the Image Matrix Generator python script (with the help of AI code assistants). It spits out the image grids in seconds, saving hours of work. If you need help running this python script, DM me on instagram and I will gladly walk you through it. Refer to the How To section where I lay out how to run the python script. 


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

## Notes

- Large matrices may result in very large output images. Adjust the settings to avoid oversized files.
- Ensure that both the input and output folders exist before generating the matrix.

## License

This project is licensed under the MIT License.
