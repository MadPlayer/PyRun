import zlib

def hash_crc32_data(data):
    binary = str(data).encode()
    return hex(zlib.crc32(binary))
