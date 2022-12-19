from skimage.viewer import ImageViewer
from skimage.io import imread

img = imread('data.jpeg')  # path to IMG
view = ImageViewer(img)
view.show()
