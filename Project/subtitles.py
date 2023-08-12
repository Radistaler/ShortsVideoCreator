from PIL import Image, ImageDraw, ImageFont


def splitter():
    
    pass

"""

Creates Mr. Beast style subtitle text

"""

def CreateSub():
    text = "There is a person standing by a big red button that will make all human life disappear including their own. You have one minute to convince them not to. What do you say?"
    font_size = 36
    font_path = "Fonts\KOMIKAX_.ttf"
    text_color = (
        255,
        255,
        255,
        255,
    )  # White color for the text with alpha channel (RGBA)
    stroke_color = (
        0,
        0,
        0,
        255,
    )  # Black color for the stroke with alpha channel (RGBA)
    stroke_width = 3

    # Load the font
    font = ImageFont.truetype(font_path, font_size)

    # Calculate text size using font.getbbox()
    text_bbox = font.getbbox(text)
    text_width = text_bbox[2] - text_bbox[0] + stroke_width * 2
    text_height = text_bbox[3] - text_bbox[1] + stroke_width * 2

    # Create a new image with a transparent background
    image = Image.new(
        "RGBA", (text_width, text_height), (0, 0, 0, 0)
    )  # Transparent background
    draw = ImageDraw.Draw(image)

    # Draw the stroke
    for x_offset in range(-stroke_width, stroke_width + 1):
        for y_offset in range(-stroke_width, stroke_width + 1):
            draw.text(
                (
                    stroke_width + x_offset - text_bbox[0],
                    stroke_width + y_offset - text_bbox[1],
                ),
                text,
                font=font,
                fill=stroke_color,
            )

    # Draw the actual text
    draw.text(
        (stroke_width - text_bbox[0], stroke_width - text_bbox[1]),
        text,
        font=font,
        fill=text_color,
    )
    # Save or display the image
    image.save("text_with_stroke_transparent.png")
    image.show()
