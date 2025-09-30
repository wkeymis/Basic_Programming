# Question

### Image Analysis of Colony Samples

You are given a text file containing RGB pixel data for multiple colony samples.  
Each sample starts with a line `"Sample: <sample_name>"` followed by rows of pixels.  
Each pixel is represented as an RGB triplet (`R,G,B`) separated by spaces.

For example, the file `file.txt`


---

## Your Task

Design a Python class `PixelManager` that:

1. Reads the pixel data from the file and stores it per sample.  
2. Provides the following methods for each sample:
   - `average_brightness(sample_name)`: Returns the average pixel brightness.  
   - `dominant_color(sample_name)`: Returns the dominant color (`Red`, `Green`, or `Blue`).  
   - `color_histogram(sample_name)`: Returns the sum of R, G, B values across all pixels.  
   - `invert_colors(sample_name)`: Returns the inverted RGB values for all pixels.  
   - `threshold(sample_name, cutoff=128)`: Converts pixels to binary based on brightness threshold.  
   - `grayscale(sample_name)`: Returns a grayscale version of the image.  
   - `is_uniform(sample_name, tolerance=10)`: Checks if all pixels are approximately the same color.  
   - `brightest_pixel(sample_name)`: Returns the coordinates and brightness of the brightest pixel.  
   - `compare_samples(sample1, sample2)`: Returns the difference in average brightness.  
   - `colony_area(sample_name, threshold=128)`: Counts pixels above the threshold (bright pixels → colony area).  
   - `average_fluorescence(sample_name)`: Returns the average brightness (proxy for fluorescence).  
   - `compare_expression(sample1, sample2)`: Returns the ratio of average brightness between two samples.  

---

## Tasks

1. Implement the `PixelManager` class.  
2. Demonstrate its functionality on the provided `file.txt` using:
   - Average brightness for each colony  
   - Dominant color per colony  
   - Brightest pixel location and value  
   - Colony area based on brightness threshold  
   - Comparison of average fluorescence between samples  

---
