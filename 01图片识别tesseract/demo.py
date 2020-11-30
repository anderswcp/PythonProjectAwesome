import tesserocr

from PIL import Image

# 获取 tesserocr 版本信息
print(tesserocr.tesseract_version())

print(tesserocr.get_languages())

image = Image.open('CheckCode.jpg')

print(tesserocr.image_to_text(image))
# print ocr text from image

print(tesserocr.file_to_text('CheckCode.jpg'))
