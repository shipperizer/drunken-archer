def encode_to_url(name):
    return name.replace(' ','_')

def decode_url(url):
    return url.replace('_',' ')
    