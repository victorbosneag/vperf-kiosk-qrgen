import segno
from PIL import Image, ImageOps
from PIL import ImageFont
from PIL import ImageDraw 
from textwrap3 import wrap
import io

FONT = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf"

def create_card(input_text, input_id):
	qrcode = segno.make("{" + '"name":"' + input_text +'","id":' + str(input_id) + "}", error='h')
	out = io.BytesIO()
	qrcode.save(out, scale=5, kind='png', dark="#475574")
	out.seek(0)
	img = Image.open(out).convert('RGB')

	logo = Image.open("logo2.png").convert('RGBA')
	logo_aspect_ratio = logo.width / logo.height
	logo = logo.resize((int(logo_aspect_ratio * (img.height//4)),img.height//4),Image.LANCZOS)


	bg_img = Image.new('RGB', (img.width + logo.width + 15, 245), "white")
	bg_img.paste(img, (0,0))
	bg_img.paste(logo,(img.width+10, 20), mask=logo)

	draw = ImageDraw.Draw(bg_img)
	font = ImageFont.truetype(FONT, 25, encoding='unic')
	id_font = ImageFont.truetype(FONT, 15, encoding='unic')

	offset = 20 + img.height//4 + 10

	for line in wrap(input_text, width=35):
	    draw.text((img.width+10+8, offset), line, font=font, fill="#475574")
	    offset += font.getsize(line)[1]

	draw.text((bg_img.width-25, bg_img.height-20), str(input_id), font=id_font, fill="#000000")


	bg_img.save(f"qrcodes/{input_id} - {input_text}.png")
