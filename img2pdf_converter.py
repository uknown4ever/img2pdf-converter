import img2pdf
import os

def main():
    # Fixed folder name
    folder_name = "my_images"
    
    # Check if the folder exists
    if not os.path.exists(folder_name):
        print(f"Error: '{folder_name}' folder does not exist")
        print(f"Please create a '{folder_name}' folder and add your images to it")
        return
    
    if not os.path.isdir(folder_name):
        print(f"Error: '{folder_name}' exists but is not a folder")
        return
    
    # Collect all image files
    imgs = []
    for fname in sorted(os.listdir(folder_name)):
        # Support multiple image formats
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        path = os.path.join(folder_name, fname)
        
        if os.path.isdir(path):
            continue
        
        imgs.append(path)
    
    # Check if any images were found
    if not imgs:
        print(f"Error: No image files found in '{folder_name}' folder")
        print("Supported formats: .jpg, .jpeg, .png")
        return
    
    # Create PDF from images
    try:
        with open("output.pdf", "wb") as f:
            f.write(img2pdf.convert(imgs))
        print(f"Success! Created output.pdf from {len(imgs)} image(s)")
        print(f"Images converted: {', '.join([os.path.basename(img) for img in imgs])}")
    except Exception as e:
        print(f"Error creating PDF: {e}")

if __name__ == "__main__":
    main()
