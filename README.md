# Video Processing Pipeline

## Description
This project implements a video processing pipeline that applies several filters to a real-time video stream. It includes filters such as mirror, fisheye, black and white, and pixelation. The original video, filtered versions, and combined output are displayed.

## Features
- Capture video from the camera.
- Apply filters:
  - Mirror filter
  - Fisheye filter
  - Black and white filter
  - Pixelation
- Display original and filtered videos in separate windows.

## Installation

1. Download or clone this repository to your computer.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the main file:

   ```bash
   python main.py
   ```

2. The program will start capturing video from your camera and applying the specified filters.

3. Video windows:
   - **Original Video**: Displays the raw video stream.
   - **Mirrored Video**: Applies a mirror filter to the original.
   - **Black and White Video**: Applies a black and white filter to the mirrored video.
   - **Fisheye Video**: Applies a fisheye filter to the black and white video.
   - **Tiled Video**: Applies a pixelation filter.
   - **Combined Output**: Shows the resulting video after applying all filters.


## Notes
- Make sure your camera is connected and accessible.
- To exit the program, press `q`.

