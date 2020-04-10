import zlib

original_data = open('data.txt','rb').read()
compressed_data = zlib.compress(original_data, zlib.Z_BEST_COMPRESSION)

compression_ratio = (float(len(original_data))-float(len(compressed_data)))/float(len(original_data))

print('Compressed : %d' % ( compression_ratio))
print('Compressed : %d%%' % (100.0 * compression_ratio))


temp_data= 'Heellllloooaxajgxjagxhjagjhg'
compressed_temp_data = zlib.compress(temp_data, 2)
f = open('outfile.txt', 'w')  
f.write(compressed_data) 
print(f"{temp_data}")


