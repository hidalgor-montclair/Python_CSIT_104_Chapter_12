# Open the bitmap file in binary mode
with open("D:\Github\PWA_Project\Python_CSIT_104_Chapter_12\CH_12.1_Reading_Files\smiley\smiley.bmp", "rb") as f:
    # Read the entire file into memory
    data = f.read()

# BMP format has a header that we need to skip to get to pixel data
# Typically, pixel data starts at offset 54 in BMP files
# pixel_data_offset = int.from_bytes(data[10:14], byteorder="little")

pixel_data_offset = 54
# print("info:")
# print(pixel_data_offset)

# Extract pixel data starting from the offset
pixel_data = data[pixel_data_offset:]

# BMP files usually store pixel data bottom-up by rows, and might have padding
# This example assumes a simple 24-bit BMP file with no padding for a small image

# Define width and height for an 8x8 image
width, height = 8, 8
pixel_size = 3  # 3 bytes per pixel for RGB

# Print the 8x8 matrix
print("8x8 Pixel Matrix:")
for row in range(height):
    row_data = []
    for col in range(width):
        # Calculate the start index for each pixel
        start_index = (row * width + col) * pixel_size
        pixel = pixel_data[start_index:start_index + pixel_size]
        # Represent each pixel as a bytes object
        row_data.append(f"{pixel}")
    # Join each row's data and print
    print(" ".join(row_data))
