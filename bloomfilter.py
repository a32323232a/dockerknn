import hashlib
import string
import random
import time
import rappor
class BloomFilter:

  # to initialize bloom filter with customed array size and hash functions.
  def __init__(self, size = 256, hash =3):
    self.one=0
    self.size = size
    self.array = [0] * size
    self.hashs = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384,hashlib.sha512,hashlib.sha3_224,hashlib.sha3_256,hashlib.sha3_384,hashlib.sha3_512,hashlib.blake2b,hashlib.blake2s]
    if hash > 12:
      print('Amount of hash functions should be less than 5. Set to 5.')
    else:
      self.hashs = self.hashs[:hash]
    return

  # to convert data with hash functions and set the filter.
  def add_data(self, data,m=110):
      
      #for i in range(10):
      #    d=(data+str(i)).encode('utf-8')
      #    for hash_func in self.hashs:
      #        idx = int(hash_func(d).hexdigest(), 16) % self.size
       #       if(self.array[idx]!=1):
      #            self.array[idx] = 1
       #           self.one+=1
      
      i=0
      while(self.one<m):
          d=(data+str(i)+'s').encode('utf-8')
          for hash_func in self.hashs:
            idx = int(hash_func(d).hexdigest(), 16) % self.size
            if(self.array[idx]!=1):
                self.array[idx] = 1
                self.one+=1
          i+=1
      return self.array


#測試false negative rate of the filter.
'''
  # to check if data can pass the filter. 
  def is_exist(self, data):
    data = data.encode('utf-8')
    for hash_func in self.hashs:
      idx = int(hash_func(data).hexdigest(), 16) % self.size
      if not self.array[idx]:
        return False
    return True

  # to test the fail negative rate of the filter.
  def test(self):
    start_time = time.time()
    true = len([bit for bit in self.array if bit])
    print('There are {} True in the {} bit.'.format(true, self.size))
    print('With {} hash functions, calculated false negative rate is {:2.5f}%.'.format(len(self.hashs), (true / self.size) ** len(self.hashs) * 100))

    fail, tests = 0, 1000000
    for _ in range(tests):
      if bloom.is_exist(randomString(random.randint(5,15))):
        fail += 1
    print('In {} test cases, the false negative rate is {:2.5f}%.'.format(tests, fail / tests * 100))
    print('This test takes {:.2f}s'.format(time.time()-start_time))
'''



'''
bloom = BloomFilter()
text = '4.6'
print('text: ',text)
k = bloom.add_data(text)
print('bloom filter:')
print(k)
'''






