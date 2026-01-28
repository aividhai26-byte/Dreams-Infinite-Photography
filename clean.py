import os

# The path to your images folder
folder_path = r'D:\dreamsweb\dreams-infinite-photography\assets\images'

# List of extensions you want to DELETE
extensions_to_delete = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.ARW']

def cleanup_images(path):
    print(f"Starting cleanup in: {path}")
    count = 0
    
    # Walk through the main folder and all subfolders (01, 02, etc.)
    for root, dirs, files in os.walk(path):
        for file in files:
            # Check if the file ends with any of the unwanted extensions
            if any(file.endswith(ext) for ext in extensions_to_delete):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file}")
                    count += 1
                except Exception as e:
                    print(f"Error deleting {file}: {e}")
                    
    print(f"--- Finished! Deleted {count} files. ---")

if __name__ == "__main__":
    if os.path.exists(folder_path):
        cleanup_images(folder_path)
    else:
        print("Error: Folder path not found. Check the path in the script.")