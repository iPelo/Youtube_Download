<h1 align="center">
  <a href="https://github.com/iPelo/Youtube_Download">
    YOUTUBE-DOWNLOAD
  </a>
</h1>

<p align="center">Simple YouTube Downloader using yt-dlp with Automatic MP4 Compatibility</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/iPelo/Youtube_Download?style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/github/languages/top/iPelo/Youtube_Download?style=for-the-badge" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/iPelo/Youtube_Download?style=for-the-badge" alt="Language Count">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Python">
  <img src="https://img.shields.io/badge/yt--dlp-FF0000?style=for-the-badge" alt="yt-dlp">
  <img src="https://img.shields.io/badge/FFmpeg-007808?style=for-the-badge" alt="FFmpeg">
  <img src="https://img.shields.io/badge/macOS-Compatible-black?style=for-the-badge" alt="macOS">
</p>

<hr>

<h2>📑 Table of Contents</h2>

<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#project-structure">Project Structure</a></li>
  <li>
    <a href="#getting-started">Getting Started</a>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
      <li><a href="#installation">Installation</a></li>
      <li><a href="#usage">Usage</a></li>
    </ul>
  </li>
  <li><a href="#notes">Notes</a></li>
</ul>

<hr>

<h2 id="overview">📜 Overview</h2>

<p><strong>Youtube-Download</strong> is a lightweight Python-based YouTube downloader built around <strong>yt-dlp</strong>.</p>

<p>The script:</p>

<ul>
  <li>Automatically selects the best compatible video format</li>
  <li>Forces H.264 (avc1) when possible</li>
  <li>Recodes to MP4 for maximum macOS / QuickTime compatibility</li>
  <li>Prevents accidental overwrites</li>
  <li>Handles both terminal and non-interactive environments (e.g., VS Code Run)</li>
</ul>

<p>All downloaded files are saved inside:</p>

<pre><code>downloads/
</code></pre>

<hr>

<h2 id="features">✨ Features</h2>

<ul>
  <li>🎥 High-quality video download</li>
  <li>🔄 Automatic MP4 recoding (<code>--recode-video mp4</code>)</li>
  <li>🖥 Works in terminal and VS Code</li>
  <li>📂 Automatic <code>downloads/</code> folder creation</li>
  <li>🚫 Prevents overwriting existing files</li>
  <li>🧠 Smart input detection (CLI argument / terminal input / GUI fallback)</li>
</ul>

<hr>

<h2 id="project-structure">📁 Project Structure</h2>

<pre><code>Youtube_Download/
│
├── download_youtube.py
├── downloads/
└── .gitignore
</code></pre>

<hr>

<h2 id="getting-started">🚀 Getting Started</h2>

<h3 id="prerequisites">📦 Prerequisites</h3>

<ul>
  <li><strong>Python 3.10+</strong></li>
  <li><strong>yt-dlp</strong></li>
  <li><strong>ffmpeg</strong> (required for recoding)</li>
</ul>

<hr>

<h3 id="installation">⚙ Installation</h3>

<pre><code class="language-bash"># Clone the repository
git clone https://github.com/iPelo/Youtube_Download.git

# Enter the project directory
cd Youtube_Download

# Install yt-dlp + ffmpeg (Homebrew)
brew install yt-dlp ffmpeg

# OR install yt-dlp via pip
python3 -m pip install -U yt-dlp
</code></pre>

<hr>

<h3 id="usage">▶ Usage</h3>

<p><strong>Option 1 — Pass URL directly</strong></p>

<pre><code class="language-bash">python3 download_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"
</code></pre>

<p><strong>Option 2 — Interactive (Terminal)</strong></p>

<pre><code class="language-bash">python3 download_youtube.py
</code></pre>

<p>Paste the URL when prompted.</p>

<p><strong>Option 3 — VS Code Run/Debug</strong></p>

<p>If stdin is not available, a GUI input window will appear automatically.</p>

<hr>

<h2 id="notes">📌 Notes</h2>

<ul>
  <li>Videos are automatically recoded to <strong>MP4 (H.264 + AAC)</strong> for compatibility.</li>
  <li>Requires <strong>ffmpeg</strong> installed and accessible in PATH.</li>
  <li>Media files are excluded from git via <code>.gitignore</code>.</li>
</ul>
