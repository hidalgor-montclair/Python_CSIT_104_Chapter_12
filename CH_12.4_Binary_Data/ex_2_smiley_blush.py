# Open the original bitmap file in binary mode
with open("D:\\Github\\PWA_Project\\Python_CSIT_104_Chapter_12\\CH_12.1_Reading_Files\\smiley\\smiley.bmp", "rb") as f:
    # Read the entire file into memory
    data = f.read()

# BMP format has a header that we need to skip to get to pixel data
# Typically, pixel data starts at offset 54 in BMP files
pixel_data_offset = 54

# Extract pixel data starting from the offset
pixel_data = bytearray(data[pixel_data_offset:])  # Convert to bytearray for mutability

# Define width and height for an 8x8 image
width, height = 8, 8
pixel_size = 3  # 3 bytes per pixel for RGB

# Iterate through each pixel in the 8x8 matrix
for row in range(height):
    for col in range(width):
        # Calculate the start index for each pixel
        start_index = (row * width + col) * pixel_size
        pixel = pixel_data[start_index:start_index + pixel_size]
        
        # Check if the pixel is black (b'\x00\x00\x00')
        if pixel == b'\x00\x00\x00':
            # Replace black pixel with red (b'\x00\x00\xFF')
            pixel_data[start_index:start_index + pixel_size] = b'\x00\x00\xFF'

# Create a new byte array for the modified image
new_data = bytearray(data)  # Start with the original data
new_data[pixel_data_offset:] = pixel_data  # Replace pixel data with modified data

# Save the modified bitmap file
with open("D:\\Github\\PWA_Project\\Python_CSIT_104_Chapter_12\\CH_12.1_Reading_Files\\smiley\\smiley_red.bmp", "wb") as f:
    f.write(new_data)

print("Modified bitmap file created: smiley_red.bmp")
