# Audiobook Creator

This is a simple Python GUI application that converts text files into audiobooks. It uses Google's Text-to-Speech (gTTS) library to generate the audiobook and provides options to select the text file, choose a save location, and play the audiobook directly.

## Features

- **Select Text File**: Choose any `.txt` file to be converted into an audiobook.
- **Choose Save Location**: Save the generated audiobook in your preferred location and specify the filename.
- **Create Audiobook**: Convert the selected text file into an audiobook (MP3 format).
- **Play Audiobook**: Listen to the audiobook once it's created.

## Prerequisites

- Python 3.x
- `gtts` library
- `tkinter` library (pre-installed with Python on most systems)

## Installation

1. Clone this repository or download the script.
2. Install the `gtts` library using pip:

   ```bash
   pip install gtts
