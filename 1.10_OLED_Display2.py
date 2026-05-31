import os
import sys
os.chdir('/tmp')
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


WIDTH = 128
HEIGHT = 64


i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)


oled.fill(0)       
oled.contrast(150) 
oled.show()


image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)


font = ImageFont.load_default()

def getfontsize(font, text):
    
    left, top, right, bottom = font.getbbox(text)
    return right - left, bottom - top





draw.rounded_rectangle([(0, 0), (oled.width - 1, oled.height - 1)], radius=4, outline=255, fill=0)


draw.line([(5, 18), (oled.width - 6, 18)], fill=255, width=1)


draw.rectangle([(10, 26), (25, 41)], fill=255) 
draw.ellipse([(10, 45), (25, 60)], outline=255) 


title_text = "ADAFRUIT"
(t_width, t_height) = getfontsize(font, title_text)

draw.text((oled.width // 2 - t_width // 2, 4), title_text, font=font, fill=255)


draw.text((32, 29), "Rendszer: OK", font=font, fill=255)
draw.text((32, 48), "USB: Aktiv", font=font, fill=255)



oled.image(image)
oled.show()
