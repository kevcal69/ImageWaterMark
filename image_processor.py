from PIL import Image

# some variables
ASSETS_DIR = 'assets/'
RESIZE_FACTOR = .3
FILEOUTPUT_PATH = 'assets/pr/'
FILEOUTPUT_NAME = 'out.png'

# import the watermark image
logo = Image.open(ASSETS_DIR + 'logo.png', 'r')
img_w, img_h = logo.size

# import the image to be watermarked
bg = Image.open(ASSETS_DIR + 'main.jpg', 'r')
bg_w, bg_h = bg.size


# calculate stuff
nlogoW = int(RESIZE_FACTOR * bg_w)
nlogoH = int(float(img_h) / float(img_w) * nlogoW)
nlogo = logo.resize((nlogoW, nlogoH), Image.ANTIALIAS)

# paste the watermark image to lower left
# with 3% of the bigger image margin
pos = (int(bg_w * .03), (bg_h - (int(bg_h * .03) + nlogoH)))
bg.paste(nlogo, pos, nlogo)

bg.save(FILEOUTPUT_PATH + FILEOUTPUT_NAME)
