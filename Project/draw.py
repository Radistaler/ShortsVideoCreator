from PIL import Image, ImageDraw, ImageFont, ImageOps


def draw_wrapped_text(draw, text, position, font, max_width, text_color):
    words = text.split()
    lines = []
    current_line = words[0]
    for word in words[1:]:
        if draw.textlength(current_line + " " + word, font=font) <= max_width:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)
    lines.reverse()
    print(lines)
    for line in lines:
        draw.text((position[0], position[1]), line, fill=text_color, font=font)
        position[1] -= font.size * 1.25


# Create a blank image
width, height = 1080, 760
background_color = (22, 22, 22)  # Dark background color
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Define colors
title_color = (255, 255, 255)  # White
details_color = (170, 170, 170)  # Light gray
icons_color = (255, 0, 0)  # Red
line_color = (100, 100, 100)  # Gray

# Load fonts
title_font = ImageFont.truetype("arial.ttf", 40)
title_font_bold = ImageFont.truetype("arialbd.ttf", 40)
details_font = ImageFont.truetype("arial.ttf", 20)
icons_font = ImageFont.truetype("arial.ttf", 25)

# Define post details
post_title = "This is an Example of a Longer Title That Needs to Wrap"
user_name = "u/PhotographyEnthusiast"
upvotes = 1350

# Calculate vertical positions
total_height = height
ui_height = 220
top_margin = (total_height - ui_height) // 2
user_y = top_margin + ui_height * 0.65
title_y = user_y - 50
icons_y = title_y + 40
line_y = icons_y + 30

# Draw post elements
draw.text((20, user_y), user_name, fill=details_color, font=details_font)

# Draw wrapped title
max_title_width = width - 40
draw_wrapped_text(
    draw, post_title, [20, title_y], title_font_bold, max_title_width, title_color
)

upvote_icon = "\u25B2"  # Upwards-pointing triangle symbol
downvote_icon = "\u25BC"  # Downwards-pointing triangle symbol

# Calculate horizontal positions
vote_margin = 15
vote_x = 20 + draw.textlength(user_name, font=details_font) + vote_margin

# Draw upvotes and downvotes
draw.text(
    (vote_x, user_y),
    f"{upvote_icon} {upvotes} {downvote_icon}",
    fill=icons_color,
    font=icons_font,
)

# Draw a horizontal line
draw.line([(20, line_y), (width - 20, line_y)], fill=line_color, width=2)

# Display an example image (optional)
image.show()
