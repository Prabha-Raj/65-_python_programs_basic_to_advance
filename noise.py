from wand.image import Image
 
# Read image using Image() function
with Image(filename ="prabhakar.jpeg") as img:
 
    # Generate noise image using noise() function
    img.noise("poisson", attenuate = 0.9)
    img.save(filename ="noisedemo.jpeg")