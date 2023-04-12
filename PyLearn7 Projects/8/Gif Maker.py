import os
import imageio.v2

file_list = sorted(os.listdir("pictures"))

images = []
for file_name in file_list:
    file_path = "pictures/" + file_name
    image = imageio.v2.imread(file_path)
    images.append(image)

imageio.v2.mimsave("Animals.gif", images, duration=3)
print("Gif is Ready!!!")
