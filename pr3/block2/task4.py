from PIL import Image

def get_image_array(file_name):
    image = Image.open(file_name)
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == 'RGB':
        channels = 3
    elif image.mode == 'RGBA':
        channels = 4
    else:
        raise ValueError("Неподдерживаемый формат изображения")
    pixel_values = [list(pixel_values[i:i+width]) for i in range(0, len(pixel_values), width)]
    return [[pixel_values[j][i][:channels] for i in range(width)] for j in range(height)]

image_array = get_image_array('screenshot-32.png')
print(image_array[:15])