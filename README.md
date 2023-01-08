# StructuralSimilarity

The project's goal was to detect differences between two images, one original and one edited. The requirement was to avoid the usage of loops, comparison of images pixel by pixel, and hardcoding of constants.

The proposed solution is to develop own version of Wang et al.'s structural similarity algorithm. The algorithm in this program calculates the gradient mask of the difference between pictures. Moreover in swiateczne.py applied is treshold with gradient mean value, floodfill algorithm, enclosion of large shapes by mean of area, removal of background, and ROI extraction. 

Example of usage:

Original image:
![org](https://user-images.githubusercontent.com/83645103/211214341-2e45a240-0b0e-47df-a119-1c701a3cf05b.jpg)

Edited image:
![edited](https://user-images.githubusercontent.com/83645103/211214414-bb78a55c-cb05-46d9-a7d9-9423c862a878.jpg)

Edited with ROIs:
![editedWithGrinches](https://user-images.githubusercontent.com/83645103/211214419-e16e0c4b-01a0-4971-b4ce-22177327262f.jpg)

Only ROIs:
![allGrinchesInOneNoBackground](https://user-images.githubusercontent.com/83645103/211214432-dba4ce3d-94eb-498b-9226-cce253c9d515.jpg)

Biggest ROI:
![biggestGrinchNoBackground](https://user-images.githubusercontent.com/83645103/211214442-047d393d-585a-4f43-bc8f-c0c948d1c225.jpg)
