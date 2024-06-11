import os
import shutil

# Define the path to the desktop
desktop_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

# Define file type categories and their corresponding folders
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Text Files': ['.txt', '.md', '.rtf'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.js', '.sh', '.bat']
}

# Create directories for file categories if they don't exist
for category in file_categories:
    category_path = os.path.join(desktop_path, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

# Function to move files to their respective folders
def move_file(file_name, file_extension):
    for category, extensions in file_categories.items():
        if file_extension in extensions:
            target_folder = os.path.join(desktop_path, category)
            target_path = os.path.join(target_folder, file_name)

            # If file already exists, append a number to the filename
            if os.path.exists(target_path):
                base_name, extension = os.path.splitext(file_name)
                counter = 1
                while os.path.exists(target_path):
                    new_file_name = f"{base_name} ({counter}){extension}"
                    target_path = os.path.join(target_folder, new_file_name)
                    counter += 1

            shutil.move(os.path.join(desktop_path, file_name), target_path)
            break

# Iterate through the files on the desktop and move them
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)
    if os.path.isfile(item_path):
        file_name, file_extension = os.path.splitext(item)
        move_file(item, file_extension)

print("Desktop cleaned and files organized into respective folders.")
