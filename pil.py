from PIL import Image, ImageDraw, ImageFont, ImageEnhance

import Image
import ImageDraw
import ImageFont

def getSize(txt, font):
    testImg = Image.new('RGB', (1, 1))
    testDraw = ImageDraw.Draw(testImg)
    return testDraw.textsize(txt, font)

if __name__ == '__main__':

    #fontname = "Arial.ttf"
    fontname = 'wqy-zenhei.ttc'
    fontsize = 12
    text = "BSP BSP BSP BSP"

    colorText = "#EFEFEF"
    colorOutline = "red"
    colorBackground = "#0088BB"


    font = ImageFont.truetype(fontname, fontsize)
    width, height = getSize(text, font)
    img = Image.new('RGB', (width+4, height+4), colorBackground)
    d = ImageDraw.Draw(img)
    d.text((2, 2), text, fill=colorText, font=font)
    #d.rectangle((0, 0, width+3, height+3), outline=colorOutline)

    img.save("image.png")
