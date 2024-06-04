# STEP 1 
# import libraries 
import fitz  # PyMuPDF
import io 
from PIL import Image 
import os

# STEP 2 
# file path you want to extract images from 
file = "Vendor Profile_Haeng Nam 17 April 2023 1.pdf"

# open the file 
pdf_file = fitz.open(file)

# Create an output directory if it doesn't exist
output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# STEP 3 
# iterate over PDF pages 
for page_index in range(len(pdf_file)): 

    # get the page itself 
    page = pdf_file[page_index] 
    image_list = page.get_images()
    
    # printing number of images found in this page 
    if image_list: 
        print(f"[+] Found a total of {len(image_list)} images in page {page_index + 1}") 
    else: 
        print(f"[!] No images found on page {page_index + 1}") 

    for image_index, img in enumerate(page.get_images(), start=1): 

        # get the XREF of the image 
        xref = img[0] 

        # extract the image bytes 
        base_image = pdf_file.extract_image(xref) 
        image_bytes = base_image["image"] 

        # get the image extension 
        image_ext = base_image["ext"]

        # create PIL Image from bytes
        image = Image.open(io.BytesIO(image_bytes))

        # save the image to the output directory with the page and image index
        image_path = os.path.join(output_dir, f"image_page{page_index + 1}_{image_index}.{image_ext}")
        image.save(image_path)

        print(f"[+] Image saved to {image_path}")