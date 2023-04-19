from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
width, height = 1200, 630
background_color = (255, 255, 255)
image = Image.new('RGB', (width, height), background_color)

# Draw on the image
draw = ImageDraw.Draw(image)

# Draw a larger smiley face with glasses and a shield
face_color = (255, 153, 51)
eye_color = (0, 0, 0)
mouth_color = (255, 0, 0)
glasses_color = (100, 100, 100)
shield_color = (50, 150, 200)

# Head
draw.ellipse((250, 100, 950, 530), fill=face_color)

# Eyes
draw.ellipse((400, 250, 480, 330), fill=eye_color)
draw.ellipse((720, 250, 800, 330), fill=eye_color)

# Glasses
draw.rectangle((380, 240, 500, 360), outline=glasses_color, width=10)
draw.rectangle((700, 240, 820, 360), outline=glasses_color, width=10)
draw.line((500, 300, 700, 300), fill=glasses_color, width=10)

# Mouth
draw.arc((400, 350, 800, 450), start=0, end=180, fill=mouth_color, width=10)




# Draw the text "Python" and a snake emoji
text_font = ImageFont.truetype("arial.ttf", 48)
emoji_font = ImageFont.truetype("NotoColorEmoji.ttf", 109)
draw.text((1020, 290), "Python", fill=(0, 0, 0), font=text_font)
snake_emoji = "\U0001F40D"
draw.text((1010, 350), snake_emoji, fill=(0, 153, 0), font=emoji_font)

# Save the image
image.save("exception_handling_smiley_shield_python_emoji.png")
