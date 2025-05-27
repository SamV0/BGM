import os
from pathlib import Path
from typing import Set, List, Optional

def print_directory_structure(
    root_dir: str | Path, 
    ignore_list: List[str], 
    output_file: Optional[str] = None,
    ignore_extensions: Optional[List[str]] = None
) -> None:
    """
    Print or save the directory structure of a given path.

    Args:
        root_dir: Root directory to start from
        ignore_list: List of directories/files to ignore
        output_file: Optional file path to save the output as markdown
        ignore_extensions: Optional list of file extensions to ignore (e.g. ['.pyc', '.log'])
    """
    root_path = Path(root_dir)
    ignore_set = {item.lower() for item in ignore_list}
    ignore_ext = {ext.lower() for ext in (ignore_extensions or [])}
    
    def should_ignore(entry: os.DirEntry) -> bool:
        return (entry.name.lower() in ignore_set or 
                any(entry.name.lower().endswith(ext) for ext in ignore_ext))
    
    output_lines = []
    
    def print_tree(path: Path, prefix: str = "") -> None:
        entries = sorted(os.scandir(path), key=lambda e: (not e.is_dir(), e.name.lower()))
        entries = [e for e in entries if not should_ignore(e)]
        
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            line = f"{prefix}{connector}{entry.name}" + ("/" if entry.is_dir() else "")
            
            if output_file:
                output_lines.append(line)
            else:
                print(line)
            
            if entry.is_dir():
                extension = "    " if is_last else "│   "
                print_tree(entry.path, prefix + extension)
    
    # Print/save the root directory name first
    root_line = f"{root_path.name}/"
    if output_file:
        output_lines.append(root_line)
    else:
        print(root_line)
        
    print_tree(root_path)
    
    # Save to markdown file if specified
    if output_file:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("```\n")
            f.write("\n".join(output_lines))
            f.write("\n```")

if __name__ == "__main__":
    # Determine project root directory
    project_directory = Path(__file__).resolve().parent
    parent_directory = project_directory.parent
    
    # Items to ignore (case-insensitive)
    ignore_items = {
        '__pycache__', 'instance', 'migrations', 
        'venv', '.git', 'misc', '.pytest_cache'
    }
    
    # File extensions to ignore
    ignore_extensions = ['.pyc', '.pyo', '.pyd', '.log']
    
    # Execute function with markdown output
    output_file = project_directory / "project_structure.md"
    print_directory_structure(
        parent_directory,
        ignore_items,
        output_file=str(output_file),
        ignore_extensions=ignore_extensions
    )

