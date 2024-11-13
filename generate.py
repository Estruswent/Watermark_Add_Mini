# coding=utf-8
from PIL import Image, ImageDraw, ImageFont
import exifread
from tkinter import Tk, filedialog, Button, Label
import os
from datetime import datetime

BORDER = 200
H_ADD = 500
H_LOGO = 230
W_LOGO = 690
PROGRAMME_FOLDER_PATH = os.getcwd()
LOGO_FOLDER_PATH = os.path.join(PROGRAMME_FOLDER_PATH, 'camera_logo')

# Choose an image and process it
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        process_image(file_path)

# Save the processed image
def save_image(image):
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG", "*.jpg")])
    if save_path:
        image.save(save_path)

# Process the image and add watermark text
def process_image(file_path):
    # Part I: Load image and EXIF data
    image = Image.open(file_path)
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)

        # 相机品牌
    camera_brand = tags.get('Image Make', 'Unknown Brand')
    logo_path = os.path.join(LOGO_FOLDER_PATH, f"{camera_brand}.png")
    if os.path.isfile( logo_path ):
        logo_image = Image.open( logo_path )
        logo_image.thumbnail( (W_LOGO, H_LOGO), Image.Resampling.LANCZOS )
        # 光圈
    aperture = tags.get('EXIF FNumber', 'Unknown Aperture')
    if aperture != 'Unknown Aperture':
        aperture = str(aperture)
        num, dem = map(float, aperture.split('/'))
        aperture = num / dem
        # 快门速度
    shutter_speed = tags.get('EXIF ExposureTime', 'Unknown Shutter Speed')
        # 焦段
    focal_length = tags.get('EXIF FocalLength', 'Unknown Focal Length')
    iso = tags.get('EXIF ISOSpeedRatings', 'Unknown ISO')
        # 时间
    phototime = tags.get('EXIF DateTimeOriginal', 'Unknown DateTime')
    if phototime != 'Unknown DateTime':
        try:
            if not isinstance(phototime, str):
                phototime = str(phototime)
            datetime_object = datetime.strptime(phototime, "%Y:%m:%d %H:%M:%S")
            datetime_str = datetime_object.strftime("%Y年%m月%d日 %H:%M:%S")
        except ValueError:
            datetime_str = "Unknown DateTime"
    else:
        datetime_str = "Unknown DateTime"
    
    # Part II: Create a new image with a white area at the bottom
    result_width = image.width + 2 * BORDER
    result_height = image.height + BORDER + H_ADD
    result = Image.new("RGB", (result_width, result_height), "white")
    result.paste(image, (BORDER, BORDER))


    # Part III: Add watermark text and draw logo
    draw = ImageDraw.Draw(result)
    font1 = ImageFont.truetype("C://windows//fonts//Bahnschrift.ttf", 144)
    font2 = ImageFont.truetype("C://windows//fonts//Simfang.ttf", 144)
    text1 = f"{focal_length}mm  F/{aperture}  {shutter_speed}s  ISO{iso}"
    text2 = f"{datetime_str}"
    logo_position = (result_width - BORDER - W_LOGO - 36, int(image.height + BORDER + 120))
    result.paste(logo_image, logo_position, logo_image.convert("RGBA"))
    draw.text((BORDER + 24, image.height + BORDER + 96), text1, fill="black", font=font1)
    draw.text((BORDER + 24, image.height + BORDER + 264), text2, fill="grey", font=font2)
    draw.text((BORDER + 23, image.height + BORDER + 264), text2, fill="grey", font=font2)
    draw.text((BORDER + 25, image.height + BORDER + 264), text2, fill="grey", font=font2)
    draw.text((BORDER + 24, image.height + BORDER + 265), text2, fill="grey", font=font2)
    draw.text((BORDER + 24, image.height + BORDER + 263), text2, fill="grey", font=font2)
    line_start = (int((result_width - 620)/ 2), int(image.height + BORDER + 50))
    line_end = (int((result_width - 620)/ 2), int(image.height + BORDER + 420))
    line_color = (200, 200, 200)
    line_width = 2
    draw.line([line_start, line_end], fill=line_color, width=line_width)
    save_image(result)

# GUI
root = Tk()
root.title("Image Watermarker")

Label(root, text="Choose an image to add watermark:").pack()
Button(root, text="Select Image", command=select_image).pack()

root.mainloop()
