from PIL import Image
import imagehash

path = 'D:/GitHub/image-hashing/img/'
images = ['python-ori.png','python-modif.png',
          'python-modif-bgt.png','php.png']
images = [path+f for f in images]

hash1 = imagehash.average_hash(Image.open(images[0]))
print('hash1 value = ',hash1)
hash2 = imagehash.average_hash(Image.open(images[1]))
print('hash2 value = ',hash2)
print('Logical equality = ', hash1 == hash2)
print('Difference Between Small Modified Images= ', abs(hash1 - hash2))

hash3 = imagehash.average_hash(Image.open(images[2]))
print('Difference Between Medium-Large Modified Images= ', abs(hash1 - hash3))

hash4 = imagehash.average_hash(Image.open(images[3]))
print('Difference Between Unrelated Images= ', abs(hash1 - hash4))