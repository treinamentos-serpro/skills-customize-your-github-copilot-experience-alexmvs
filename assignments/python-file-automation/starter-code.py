from pathlib import Path
import shutil


CATEGORY_BY_EXTENSION = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".csv": "Spreadsheets",
    ".xlsx": "Spreadsheets",
}
DESTINATION_FOLDER = "organized"


def categorize_file(file_path):
    """Return the category for a file based on its extension."""
    # TODO: Read the suffix, normalize its case, and look it up in the mapping.
    pass


def build_plan(source_dir):
    """Return (source, destination) pairs without changing any files."""
    plan = []

    # TODO: Inspect files directly inside source_dir and build destination paths.
    # Destination paths should be source_dir / DESTINATION_FOLDER / category / filename.

    return plan


def organize_files(source_dir, apply=False):
    """Print a plan, and move files only when apply is True."""
    plan = build_plan(source_dir)

    for source_path, destination_path in plan:
        print(f"{source_path.name} -> {destination_path.relative_to(source_dir)}")

        if not apply:
            continue

        # TODO: Skip existing destinations, create the category folder, then move.
        pass


def main():
    source_dir = Path(input("Folder to organize: ")).expanduser()
    if not source_dir.is_dir():
        print("The selected path does not exist or is not a folder.")
        return

    print("Preview (no files will be moved):")
    organize_files(source_dir)

    confirmation = input("Move these files? [y/N]: ").strip().lower()
    if confirmation == "y":
        organize_files(source_dir, apply=True)
    else:
        print("No files were moved.")


if __name__ == "__main__":
    main()