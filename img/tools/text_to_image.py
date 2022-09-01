from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def draw_image(text, text_width=200, text_height=50, font_type="arial.ttf", font_size=18):

    img = Image.new('RGB', (text_width, text_height), color = (255,255,255))
    font = ImageFont.truetype(font_type, font_size)
    d = ImageDraw.Draw(img)
    d.text((0,0), text, font=font, fill=(0,0,0))
    text_width, text_height = d.textsize(text, font)
    
    offset_x, offset_y = font.getoffset(text)
    text_width += offset_x
    text_height += offset_y
    
    return (img, text_width, text_height)


def text_to_image_fitting(email, filename):
   
    # First get the text size
    [img, text_width, text_height] = draw_image(email)
    # Draw with correct text size
    [img, text_width, text_height] = draw_image(email, text_width, text_height)
    
    img.save(filename, quality=95, subsampling=0)
