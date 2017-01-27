from PIL import Image

ASSETS_DIR = 'assets/'
RESIZE_FACTOR = .3
logo = Image.open(ASSETS_DIR + 'logo.png', 'r')

img_w, img_h = logo.size

bg = Image.open(ASSETS_DIR + 'main.jpg', 'r')
bg_w, bg_h = bg.size


nlogoW = int(RESIZE_FACTOR * bg_w)
nlogoH = int(float(img_h) / float(img_w) * nlogoW)

nlogo = logo.resize((nlogoW, nlogoH), Image.ANTIALIAS)

pos = (int(bg_w * .03), (bg_h - (int(bg_h * .03) + nlogoH)))
bg.paste(nlogo, pos, nlogo)
bg.save('assets/pr/out.png')
