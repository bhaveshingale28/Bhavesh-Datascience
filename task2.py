import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread("image.png")

print("Image Shape:", image.shape)

grayscale = np.mean(image[:, :, :3], axis=2)

print("Grayscale Image Shape:", grayscale.shape)

bright_image = np.clip(grayscale + 0.5, 0, 1)

dark_image = np.clip(grayscale - 0.5, 0, 1)

horizontal_flip = np.fliplr(grayscale)

vertical_flip = np.flipud(grayscale)

cropped = grayscale[100:300, 100:300]

fig, axes = plt.subplots(2, 4, figsize=(16, 8))

axes[0,0].imshow(image)
axes[0,0].set_title("Original")
axes[0,0].axis("off")

axes[0,1].imshow(grayscale, cmap='gray')
axes[0,1].set_title("Grayscale")
axes[0,1].axis("off")

axes[0,2].imshow(bright_image, cmap='gray')
axes[0,2].set_title("Bright")
axes[0,2].axis("off")

axes[0,3].imshow(dark_image, cmap='gray')
axes[0,3].set_title("Dark")
axes[0,3].axis("off")

axes[1,0].imshow(horizontal_flip, cmap='gray')
axes[1,0].set_title("Horizontal Flip")
axes[1,0].axis("off")

axes[1,1].imshow(vertical_flip, cmap='gray')
axes[1,1].set_title("Vertical Flip")
axes[1,1].axis("off")

axes[1,2].imshow(cropped, cmap='gray')
axes[1,2].set_title("Cropped")
axes[1,2].axis("off")

axes[1,3].axis("off")

plt.tight_layout()
plt.show()