import os
import subprocess
import progressbar

os.makedirs('mockups', exist_ok = True)
files = os.listdir('tiled_images')
progress = progressbar.ProgressBar(
    maxval = len(files),
    widgets = [
        progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()
    ]
)
import os
import cv2

# # Path to the folder containing images to be resized
# input_folder = "tiled_images"

# # Path to the folder where resized images will be saved
# output_folder = "tiled_images"

# Path to the template image whose shape will be used for resizing
image_path = "base_images/template_resized.jpeg"

# # Function to resize images
# def resize_images(input_folder, output_folder, template_image_path):
#     # Load the template image
#     template_image = cv2.imread(template_image_path)
#     template_height, template_width, _ = template_image.shape

#     # Loop through each file in the input folder
#     for filename in os.listdir(input_folder):
#         # Read the image
#         img_path = os.path.join(input_folder, filename)
#         img = cv2.imread(img_path)

#         # Resize the image to match the shape of the template image
#         resized_img = cv2.resize(img, (template_width, template_height))

#         # Save the resized image with the same filename in the output folder
#         output_path = os.path.join(output_folder, filename)
#         cv2.imwrite(output_path, resized_img)

# # Resize images
# resize_images(input_folder, output_folder, image_path)

for i, file in enumerate(files):
    progress.update(i)
    subprocess.call(
        [
            'sh',
            'generate_mockup.sh',
            image_path,
            'base_images/mask_resized.png',
            os.path.join('tiled_images', file),
            'maps/displacement_map.png',
            'maps/lighting_map.png',
            'maps/adjustment_map.jpg',
            os.path.join('mockups', os.path.basename(file))
        ]
    )

progress.finish()
