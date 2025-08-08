from PIL import Image, ImageDraw
import os

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def brightness_to_radius(brightness, max_radius):
    # Brightness is 0 (black) to 255 (white)
    # Darker pixels -> larger dots
    return max_radius * (1 - brightness / 255)

def render_dots(image, dot_spacing=10, max_dot_radius=5):
    width, height = image.size
    canvas_width = width * dot_spacing
    canvas_height = height * dot_spacing
    output_img = Image.new("RGB", (canvas_width, canvas_height), "white")
    draw = ImageDraw.Draw(output_img)

    for y in range(height):
        for x in range(width):
            brightness = image.getpixel((x, y))
            radius = brightness_to_radius(brightness, max_dot_radius)
            if radius > 0.5:  # Skip nearly white pixels
                center_x = x * dot_spacing + dot_spacing // 2
                center_y = y * dot_spacing + dot_spacing // 2
                draw.ellipse(
                    [(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)],
                    fill="black"
                )

    return output_img

def main():
    image_path = input("Enter the full path of the image (any format): ").strip('"')

    if not os.path.exists(image_path):
        print(" File does not exist.")
        return

    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f" Failed to open image: {e}")
        return

    # Process image
    resized_img = resize_image(image, new_width=100)  # You can change width
    gray_img = grayify(resized_img)
    dot_image = render_dots(gray_img, dot_spacing=10, max_dot_radius=5)

    # Save output
    output_path = os.path.join(os.path.dirname(image_path), "dot_art_output.jpg")
    dot_image.save(output_path)
    print(f"Dot Art saved to: {output_path}")

if __name__ == "__main__":
    main()
