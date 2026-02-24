import subprocess
import sys
from pathlib import Path


def main():
    project_folder = Path.cwd()
    output_folder = project_folder / "downloads"
    output_folder.mkdir(exist_ok=True)

    url = input("Enter YouTube URL: ").strip()
    if not url:
        print("No URL provided.")
        sys.exit(1)

    output_template = str(output_folder / "%(title)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "-f", "bv*+ba/best",
        "--merge-output-format", "mp4",
        "--restrict-filenames",
        "-o", output_template,
        url,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"\nDone. File saved in: {output_folder}")
    except FileNotFoundError:
        print("\nError: yt-dlp is not installed or not in PATH.")
        print("Install it first, then run this script again.")
        print("macOS (Homebrew): brew install yt-dlp ffmpeg")
        print("or Python: python -m pip install -U yt-dlp")
    except subprocess.CalledProcessError as e:
        print(f"\nDownload failed (exit code {e.returncode}).")


if __name__ == "__main__":
    main()