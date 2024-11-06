# Opening a file in write mode
f = open('myfile4.txt', 'w')

# Writing to the file, but it's still in the buffer
f.write('This is buffered.')

# Forcing Python to save to 'myfile.txt' immediately
f.flush()  # Save immediately without waiting for a newline!

# Closing the file also saves any remaining data in the buffer
f.close()

