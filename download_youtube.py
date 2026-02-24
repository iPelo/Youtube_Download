import subprocess
import sys
from pathlib import Path


def get_url():
    # 1) CLI argument (works everywhere)
    if len(sys.argv) >= 2 and sys.argv[1].strip():
        return sys.argv[1].strip()

    # 2) Interactive stdin (works in real terminals)
    if sys.stdin is not None and getattr(sys.stdin, "isatty", lambda: False)():
        print("Paste the YouTube URL and press Enter:", flush=True)
        try:
            url = sys.stdin.readline()
        except Exception:
            url = ""
        return (url or "").strip()

    # 3) Non-interactive consoles (e.g., VS Code Debug/Output): use a GUI prompt
    try:
        import tkinter as tk
        from tkinter import simpledialog

        root = tk.Tk()
        root.withdraw()  # hide main window

        # Convenience: prefill with clipboard text if it looks like a URL
        default_value = ""
        try:
            clip = root.clipboard_get().strip()
            if clip.startswith("http://") or clip.startswith("https://"):
                default_value = clip
        except Exception:
            pass

        url = simpledialog.askstring("YouTube Downloader", "Paste the YouTube URL:", initialvalue=default_value)
        root.destroy()
        return (url or "").strip()
    except Exception:
        # Last resort: tell user how to run
        print("Input is not available in this console.")
        print("Run in a terminal, or pass the URL as an argument:")
        print('  python3 download_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"')
        return ""


def main():
    print("YouTube downloader started", flush=True)

    project_folder = Path.cwd()
    output_folder = project_folder / "downloads"
    output_folder.mkdir(exist_ok=True)

    url = get_url()
    if not url:
        print("No URL provided.")
        print("Run like this:")
        print("  python3 download_youtube.py \"https://www.youtube.com/watch?v=VIDEO_ID\"")
        sys.exit(1)

    output_template = str(output_folder / "%(title)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "-f",
        "bv*[vcodec^=avc1][ext=mp4]+ba[ext=m4a]/bv*[vcodec^=avc1]+ba/b[ext=mp4]/b/best",
        "--merge-output-format",
        "mp4",
        "--recode-video",
        "mp4",
        "--restrict-filenames",
        "--no-overwrites",
        "-o",
        output_template,
        url,
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"\nDone. File saved in: {output_folder}")
    except FileNotFoundError:
        print("\nError: yt-dlp is not installed or not in PATH.")
        print("Install it first, then run this script again.")
        print("macOS (Homebrew): brew install yt-dlp ffmpeg")
        print("If ffmpeg is missing, merges/transcodes may fail or produce unplayable files.")
        print("or Python: python3 -m pip install -U yt-dlp")
    except subprocess.CalledProcessError as e:
        print(f"\nDownload failed (exit code {e.returncode}).")


if __name__ == "__main__":
    main()