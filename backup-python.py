import os
import shutil
import sys
import datetime

def backup_files(source_dir, destination_dir):
    
    print(f"Starting backup from '{source_dir}' to '{destination_dir}'...")

  
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    
    if not os.path.exists(destination_dir):
        print(f"Destination directory '{destination_dir}' does not exist. Creating it...")
        try:
            os.makedirs(destination_dir)
            print("Destination directory created successfully.")
        except OSError as e:
            print(f"Error: Could not create destination directory '{destination_dir}': {e}")
            return
    elif not os.path.isdir(destination_dir):
        print(f"Error: Destination path '{destination_dir}' exists but is not a directory.")
        return

    copied_count = 0
    skipped_count = 0
    error_count = 0

    try:
        for filename in os.listdir(source_dir):
            source_filepath = os.path.join(source_dir, filename)

          
            if os.path.isfile(source_filepath):
                destination_filepath = os.path.join(destination_dir, filename)

              
                if os.path.exists(destination_filepath):
                    
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    name_parts = os.path.splitext(filename)
                    new_filename = f"{name_parts[0]}_{timestamp}{name_parts[1]}"
                    destination_filepath = os.path.join(destination_dir, new_filename)
                    print(f"Conflict: '{filename}' already exists. Saving as '{new_filename}'")

                try:
                    shutil.copy2(source_filepath, destination_filepath) 
                    print(f"Copied: '{filename}' to '{destination_filepath}'")
                    copied_count += 1
                except Exception as e:
                    print(f"Error copying '{filename}': {e}")
                    error_count += 1
            else:
                print(f"Skipped: '{filename}' (not a file or is a directory).")
                skipped_count += 1

        print("\nBackup process completed.")
        print(f"Summary: Copied {copied_count} files, Skipped {skipped_count} items, Encountered {error_count} errors.")

    except OSError as e:
        print(f"Error during file processing: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main execution block
if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        print("Example: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    backup_files(source_directory, destination_directory)