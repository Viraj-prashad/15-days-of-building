import os
import shutil


# File extension categories
IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]
DOCUMENT_EXTENSIONS = [".pdf", ".docx", ".txt"]
VIDEO_EXTENSIONS = [".mp4", ".mkv"]


def transfer_file(destination_file_path, option, item, category, item_path):
    """Move or copy a single file into its category folder.

    This function does three things:
    1) Skips if the destination file already exists
    2) Copies the file when option == "copy"
    3) Moves the file when option == "move"

    Notes:
    - The caller (organize) already validates the option value.
    - Messages are printed so you can see what happened for each file.
    """
    # If a file with the same name already exists at the destination, do nothing.
    if os.path.exists(destination_file_path):
        print(f"File already exists in destination: {item}. Skipping.")
        return

    # Perform the requested action
    if option == "copy":
        shutil.copy2(item_path, destination_file_path)
        print(f"File: {item} -> {category}")
    elif option == "move":
        shutil.move(item_path, destination_file_path)
        print(f"File: {item} -> {category}")


# define the organize function
def organize():
    print("\n")
    print("############ File Organizer ############")
    print("\n")

    # Get user input for source and destination directories and action
    source_dir = input("Enter the source directory path: ").strip()
    dest_dir = input("Enter the destination directory path: ").strip()
    option = (
        input("Do you want to copy the files or move them? (copy/move): ")
        .strip()
        .lower()
    )

    # Check if source folder exists
    if not os.path.exists(source_dir):
        print("Error: Source folder does not exist.")
        return

    print("\nSource directory found.")

    # Ensure destination folder exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print("\nDestination folder created.")
    else:
        print("\nDestination folder already exists.")

    # Validate the option
    if option not in ["copy", "move"]:
        print("Error: Invalid option. Please choose 'copy' or 'move'.")
        return

    # List items in source folder
    items = os.listdir(source_dir)

    print("\nItems found in source directory:")

    for item in items:
        item_path = os.path.join(source_dir, item)

        # Process only files
        if os.path.isfile(item_path):
            _, extension = os.path.splitext(item)
            extension = extension.lower()

            # Decide category
            if extension in IMAGE_EXTENSIONS:
                category = "Images"
            elif extension in DOCUMENT_EXTENSIONS:
                category = "Documents"
            elif extension in VIDEO_EXTENSIONS:
                category = "Videos"
            else:
                category = "Other"

            # Create category folder if it doesn't exist
            category_folder = os.path.join(dest_dir, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
                print(f"Created folder: {category}")

            # Move or copy file according to user's wish to category folder
            destination_file_path = os.path.join(category_folder, item)

            transfer_file(destination_file_path, option, item, category, item_path)

        # Ignore folders
        elif os.path.isdir(item_path):
            print(f"\nDirectory: {item}\n")


if __name__ == "__main__":
    organize()
