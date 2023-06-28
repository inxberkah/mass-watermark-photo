from PIL import Image, ImageDraw, ImageFont
import os
#Author Berkah@code:~

def add_photo_watermark(input_image_path, watermark_image_path, output_image_path):
    with Image.open(input_image_path).convert("RGBA") as img:
        with Image.open(watermark_image_path).convert("RGBA") as watermark:
            watermark_size = (img.width // 4, img.height // 4)
            watermark = watermark.resize(watermark_size)
            watermark_layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
            watermark_layer.paste(watermark, (10, 10))
            watermarked_image = Image.alpha_composite(img, watermark_layer).convert("RGB")
            watermarked_image.save(output_image_path)

def add_text_watermark(input_image_path, output_image_path, watermark_text):
    with Image.open(input_image_path) as img:
        watermark = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark)
        font = ImageFont.truetype("arial.ttf", 40)
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = img.width - text_width - 10
        y = img.height - text_height - 10
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))
        watermarked = Image.alpha_composite(img.convert("RGBA"), watermark)
        watermarked.convert("RGB").save(output_image_path)

input_folder = "Your_Path_Folder_Photo"

watermark_image = "watermark.png"

output_folder = "Your_Path_Folder_Save"

print("Choose watermark type:")
print("1. Photo watermark")
print("2. Text watermark")
option = int(input("Enter your choice (1 or 2): "))

if option == 1:
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            add_photo_watermark(input_image_path, watermark_image, output_image_path)
    print("Watermarking completed.")
elif option == 2:
    watermark_text = input("Enter the watermark text: ")
    for filename in os.listdir(input_folder):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            add_text_watermark(input_image_path, output_image_path, watermark_text)
    print("Watermarking completed.")
else:
    print("Invalid option. Please choose 1 or 2.")
