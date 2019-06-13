from scipy import misc
from PIL import Image
from numpy import *
from pylab import *
import sift
imname = "D:/pygame/test.jpg"
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'test.sift')
l1,d1 = sift.read_features_from_file('test.sift')
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()