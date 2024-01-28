import shutil
import os

def copy_assets():
    # Define source and destination directories
    source_css_dir = 'css'
    source_images_dir = 'images'
    destination_static_dir = 'web_flask/static'

    # Create the destination directories if they don't exist
    os.makedirs(os.path.join(destination_static_dir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(destination_static_dir, 'styles'), exist_ok=True)

    # Get the absolute path of the current script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Copy CSS files
    css_files = ['3-footer.css', '3-header.css', '4-common.css', '6-filters.css']
    for css_file in css_files:
        source_path = os.path.join(script_directory, source_css_dir, css_file)
        destination_path = os.path.join(script_directory, destination_static_dir, 'styles', css_file)
        shutil.copy(source_path, destination_path)

    # Copy images
    image_files = ['icon.png', 'logo.png']
    for image_file in image_files:
        source_path = os.path.join(script_directory, source_images_dir, image_file)
        destination_path = os.path.join(script_directory, destination_static_dir, 'images', image_file)
        shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    copy_assets()
