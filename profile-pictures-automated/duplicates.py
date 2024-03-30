import os
from PIL import Image
import imagehash
import shutil

def hash_image(image_path):
    # Open and hash the image
    with open(image_path, 'rb') as f:
        return imagehash.average_hash(Image.open(f))

def compare_images(image1, image2):
    # Compare the hashes of two images
    return image1 == image2

def separate_duplicates_and_unique(input_folder, unique_folder, duplicate_folder):
    # Create output folders if they don't exist
    os.makedirs(unique_folder, exist_ok=True)
    os.makedirs(duplicate_folder, exist_ok=True)

    # Dictionary to store image hashes and file paths
    image_hashes = {}

    # Iterate over images in the input folder
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # Skip if the file is not an image
        if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            continue

        # Calculate the hash of the image
        image_hash = hash_image(file_path)

        # Check if the hash already exists
        if image_hash in image_hashes:
            # Move the duplicate image to the duplicate folder
            shutil.move(file_path, os.path.join(duplicate_folder, filename))
        else:
            # Store the hash and file path in the dictionary
            image_hashes[image_hash] = file_path
            # Copy the unique image to the unique folder
            shutil.copy(file_path, os.path.join(unique_folder, filename))

if __name__ == "__main__":
    input_folder = '/Users/radiohead/Downloads/slick/profile pictures/yes'  # Replace with the folder containing images
    unique_folder = '/Users/radiohead/Downloads/slick/profile pictures/unique'  # Folder for unique images
    duplicate_folder = '/Users/radiohead/Downloads/slick/profile pictures/duplicate'  # Folder for duplicate images

    separate_duplicates_and_unique(input_folder, unique_folder, duplicate_folder)