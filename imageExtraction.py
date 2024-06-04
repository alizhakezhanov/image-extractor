
import fitz 
import io 
from PIL import Image 
import os

file = "Vendor Profile_Haeng Nam 17 April 2023 1.pdf"


pdf_file = fitz.open(file)


output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for page_index in range(len(pdf_file)): 

    page = pdf_file[page_index] 
    image_list = page.get_images()
    
    if image_list: 
        print(f"[+] Found a total of {len(image_list)} images in page {page_index + 1}") 
    else: 
        print(f"[!] No images found on page {page_index + 1}") 

    for image_index, img in enumerate(page.get_images(), start=1): 
        
        xref = img[0] 

        base_image = pdf_file.extract_image(xref) 
        image_bytes = base_image["image"] 

        image_ext = base_image["ext"]

        image = Image.open(io.BytesIO(image_bytes))

        image_path = os.path.join(output_dir, f"image_page{page_index + 1}_{image_index}.{image_ext}")
        image.save(image_path)

        print(f"[+] Image saved to {image_path}")