import datetime
import hashlib
import random
import uuid
from strgen import StringGenerator

class Security:

    def __init__(self):
        self.crsf = uuid.uuid4()
        self.acess = ''

    def hash_generator_uuid(self):
        hash = uuid.uuid4()
        return hash

    def hash_generator_string(self):
        hash = StringGenerator("[\l\d]{48}")
        return hash

    def hash_generator_random(self):

        string = str(random.randrange(10000000000000001, 999999999999999999)).encode()
        hash = hashlib.md5(string).hexdigest()

        return hash