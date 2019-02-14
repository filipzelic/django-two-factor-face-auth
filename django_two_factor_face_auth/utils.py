import base64
import re
from io import BytesIO
from django.core.files.base import ContentFile

def decode_base64(data, altchars=b'+/'):
    image_data = re.sub('^data:image/.+;base64,', '', data)
    return base64.b64decode(image_data)

def prepare_image(image):
    return BytesIO(decode_base64(image))

def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))