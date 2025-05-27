import os
import re
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

IGNORE_FOLDERS = {'env', 'migrations', '__pycache__', 'node_modules', 'misc'}  # Add more folders to ignore if necessary
IGNORE_FILES = {'codestats.py', 'codestats_tk.py'}  # Add more files to ignore if necessary

def count_lines_words(filepath):
    """
    Returns a dictionary with counts of lines, words, characters,
    blank lines, and comments in a given file.
    """
    lines = words = chars = blanks = comments = 0

    # Regex for detecting Python comments. This looks for a '#' that is either at the start
    # of a line or is preceded by whitespace and not within quotes.
    python_comment_regex = re.compile(r'''(?x)
        (^\s*\#)        # Line starts with a comment
        |
        (?<!['"])\#     # A '#' not immediately preceded by a quote
    ''')

    # You may still have comment markers for other file types
    comment_markers = {'//': 'js', '/*': 'css', '<!--': 'html'}

    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                lines += 1
                words += len(line.split())
                chars += len(line)
                stripped_line = line.strip()

                if stripped_line == '':
                    blanks += 1
                else:
                    # For Python files, use the regex to detect inline and whole-line comments.
                    if filepath.endswith('.py'):
                        if python_comment_regex.search(line):
                            comments += 1
                    else:
                        # For other file types, count if the line starts with any comment marker.
                        if any(stripped_line.startswith(marker) for marker in comment_markers):
                            comments += 1
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")

    return {
        'lines': lines,
        'words': words,
        'characters': chars,
        'blank_lines': blanks,
        'comments': comments
    }

def get_files_by_extension(root_dir, extensions):
    """
    Recursively collects all files with the specified extensions in the directory.
    """
    collected_files = []
    for subdir, _, files in os.walk(root_dir):
        if any(ignored in subdir for ignored in IGNORE_FOLDERS):
            continue
        for file in files:
            if file.endswith(extensions) and file not in IGNORE_FILES:
                collected_files.append(os.path.join(subdir, file))
    return collected_files

def analyze_directory(directory):
    """
    Analyze the given directory and return statistics for all specified files as a string.
    """
    file_extensions = ('.py', '.html', '.css', '.js')
    project_files = get_files_by_extension(directory, file_extensions)

    if not project_files:
        return "No relevant files found."

    total_stats = {
        'total_lines': 0,
        'total_words': 0,
        'total_characters': 0,
        'total_blank_lines': 0,
        'total_comments': 0
    }

    output_lines = []
    output_lines.append(f"Analyzing directory: {directory}\n")

    # Sort files by number of lines
    sorted_files = sorted(project_files, key=lambda x: count_lines_words(x)['lines'])
    for filepath in sorted_files:
        stats = count_lines_words(filepath)
        total_stats['total_lines'] += stats['lines']
        total_stats['total_words'] += stats['words']
        total_stats['total_characters'] += stats['characters']
        total_stats['total_blank_lines'] += stats['blank_lines']
        total_stats['total_comments'] += stats['comments']

        output_lines.append(f"File: {filepath}")
        output_lines.append(f"  Lines: {stats['lines']}")
        output_lines.append(f"  Words: {stats['words']}")
        output_lines.append(f"  Characters: {stats['characters']}")
        output_lines.append(f"  Blank lines: {stats['blank_lines']}")
        output_lines.append(f"  Comments: {stats['comments']}")
        output_lines.append("-" * 40)

    output_lines.append("\nOverall Project Statistics:")
    output_lines.append(f"  Total lines: {total_stats['total_lines']}")
    output_lines.append(f"  Total words: {total_stats['total_words']}")
    output_lines.append(f"  Total characters: {total_stats['total_characters']}")
    output_lines.append(f"  Total blank lines: {total_stats['total_blank_lines']}")
    output_lines.append(f"  Total comments: {total_stats['total_comments']}")
    output_lines.append("=" * 40)

    return "\n".join(output_lines)

class CodeStatsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Stats Analyzer")
        self.geometry("800x600")
        self.current_directory = None
        
        # Button frame
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(button_frame, text="Select Directory", command=self.select_directory).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Refresh", command=self.refresh_analysis).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_text).pack(side=tk.LEFT, padx=5)
        
        # ScrolledText widget for output
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.current_directory = directory  # Store the selected directory for refresh
            self.run_analysis(directory)
        else:
            messagebox.showinfo("Directory selection", "No directory selected!")

    def refresh_analysis(self):
        if self.current_directory:
            self.run_analysis(self.current_directory)
        else:
            messagebox.showinfo("Refresh", "No directory has been selected yet.")

    def run_analysis(self, directory):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, "Analyzing, please wait...\n")
        self.update()  # Force UI update
        result = analyze_directory(directory)
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, result)

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

if __name__ == '__main__':
    app = CodeStatsApp()
    app.mainloop()