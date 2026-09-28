import cv2
import numpy as np
from matplotlib import pyplot as plt
def show_comparison(original,with_bg,without_bg):
  plt.figure(figsize=(15,5))
  plt.subplot(1,3,1)
  plt.imshow(original,cmap='gray')
  plt.title("Original Image")
  plt.axis('off')

  plt.subplot(1,3,2)
  plt.imshow(without_bg,cmap='gray')
  plt.title("Slicing Without Background")
  plt.axis('off')

  plt.subplot(1,3,3)
  plt.imshow(with_bg,cmap='gray')
  plt.title("Slicing With Background")
  plt.axis('off')

  plt.tight_layout()
  plt.show()
img=cv2.imread('Forest.jpg',cv2.IMREAD_GRAYSCALE)
if img is None:
  print("Error:Image not found.")
else:
  rows,cols=img.shape
  slice_without_bg=np.zeros((rows,cols),dtype=np.uint8)
  slice_with_bg=img.copy()
  min_range=100
  max_range=150
  L=255
  for i in range(rows):
    for j in range(cols):
      pixel_val=img[i,j]
      if min_range<=pixel_val<=max_range:
        slice_without_bg[i,j]=L
        slice_with_bg[i,j]=L
      else:
        slice_without_bg[i,j]=0
        slice_with_bg[i,j]=pixel_val
  show_comparison(img,slice_with_bg,slice_without_bg)
