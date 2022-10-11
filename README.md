# Music Visualization

![Visualization of *Bach Cello Suite No1 in G Major*](https://user-images.githubusercontent.com/78770681/195198413-5b138ca3-5e00-4cac-9f82-049cb6fe94e3.jpg)
*(Try making out a horizontal line in the middle of the image. Reading from left to right along the line, one can perhaps feel the change in intensity in the music piece over time. By the way, this one is Bach Cello Suite No. 1 in G Major. See more [examples](https://github.com/BenWeiTang/Music-Visualization/tree/main/Examples).)*

## Overview
This project aims to visualize audio input in a comprehensive way in terms of color theory and music theory. The process starts with anaylizing an audio file with a Python library SciPy, using Short-Time Fast Fourier Transform to identify the musical notes in the audio file. The information is then passed into Processing to generate an image as an output. Each note in a piece is an invisible, drifting circle, and when two circles overlap, a line is drawn between their centers. The color of the line is determined by the interval between those two notes. The intervals on the Circle of Fifth are mapped to a color wheel, where a perfect unison corresponds to white and furthering away from the perfect unison results in more vibrant colors.

## Instruction
