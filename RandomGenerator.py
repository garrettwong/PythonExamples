import random
import string

class RandomGenerator:
    def getRandomString(self, len):
        rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
        
        # Now to generate a random string of length 10
        s = rand_str(len)

        return s

    # returns a number in the range [min, max)
    def getRandomNumber(self, min, max):
        return random.randint(min, max-1)

    # returns a number in the range [0.0, 1.0)
    def getRandomDouble(self):
        return random.random()


# main
if __name__ == "__main__":
    rsg = RandomGenerator()
    print(rsg.getRandomString(14))
    print(rsg.getRandomNumber(12, 15))
    print(rsg.getRandomDouble())