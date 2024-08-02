from PIL import Image, ImageDraw

def create_frog_image(filename, width=100, height=100):
    # Create a new image with a transparent background
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    body_color = (34, 139, 34, 255)  # Forest green
    eye_color = (255, 255, 255, 255)  # White
    pupil_color = (0, 0, 0, 255)      # Black
    leg_color = (0, 100, 0, 255)      # Dark green

    # Draw the body of the frog
    body_box = [width*0.25, height*0.35, width*0.75, height*0.75]
    draw.ellipse(body_box, fill=body_color, outline=(0, 100, 0))

    # Draw the eyes
    eye_box1 = [width*0.35, height*0.20, width*0.45, height*0.30]
    eye_box2 = [width*0.55, height*0.20, width*0.65, height*0.30]
    draw.ellipse(eye_box1, fill=eye_color)
    draw.ellipse(eye_box2, fill=eye_color)
    
    # Draw pupils
    pupil_box1 = [width*0.37, height*0.22, width*0.43, height*0.28]
    pupil_box2 = [width*0.57, height*0.22, width*0.63, height*0.28]
    draw.ellipse(pupil_box1, fill=pupil_color)
    draw.ellipse(pupil_box2, fill=pupil_color)
    
    # Draw the legs
    # Front legs
    draw.rectangle([width*0.20, height*0.75, width*0.30, height*0.85], fill=leg_color)
    draw.rectangle([width*0.70, height*0.75, width*0.80, height*0.85], fill=leg_color)
    
    # Back legs
    draw.rectangle([width*0.15, height*0.80, width*0.25, height*0.90], fill=leg_color)
    draw.rectangle([width*0.75, height*0.80, width*0.85, height*0.90], fill=leg_color)

    # Save the image
    img.save(filename)

# Create and save the frog image
create_frog_image('frog.png')
