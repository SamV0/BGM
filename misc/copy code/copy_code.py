import os

# Define source directory and output file
SOURCE_DIR = r"C:\Users\samar\Documents\BGM"
OUTPUT_FILE = r"C:\Users\samar\Documents\BGM\misc\copy code\copies\all_code_combined.txt"

# Excluded directories
EXCLUDED_DIRS = {"misc", "venv", "__pycache__", "instance"}

def collect_code_and_paths(source_dir):
    collected_data = []

    for root, dirs, files in os.walk(source_dir):
        # Remove excluded directories from the search
        dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                content = f"ERROR READING FILE: {str(e)}"
            # Append the full file path and content
            collected_data.append((file_path, content))
    return collected_data

def write_combined_file(output_file, collected_data):
    with open(output_file, "w", encoding="utf-8") as out_file:
        for full_path, content in collected_data:
            # Find the index of "app" to get the relative path
            idx = full_path.find("BGM")
            relative_path = full_path[idx:] if idx != -1 else full_path
            out_file.write(f"#{relative_path}\n")
            out_file.write(content + "\n")

if __name__ == "__main__":
    data = collect_code_and_paths(SOURCE_DIR)
    write_combined_file(OUTPUT_FILE, data)
    print(f"Code copied to {OUTPUT_FILE}")