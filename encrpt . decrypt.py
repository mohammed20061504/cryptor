import base64

options = input("""

1 >> encode

2 >> decode
""")

if options == "1":
    encode_text = input("enter your text for encode it :")
    encode_hash = base64.b64encode(encode_text.encode('UTF-8')).decode('ascii')
    print("------------------------------")
    print(encode_hash)
elif options == "2":
    decode_text = input("enter your text for decode it :")
    decode_hash = base64.b64decode(decode_text)
    decodeit = decode_hash.decode('UTF-8')
    print(decodeit)
else:
    print("error")
