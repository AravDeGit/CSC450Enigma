import random
class Enigma:
    def key():
        keyList = []
        rand = random.randint(10000, 99999) # General soltuion : argument: n for the number of digits, use n as a power of 10 for lower and upper limit. 
        free = rand
        while free > 10:
            div = 100 # General solution: use n-1 power of 10 and keep dividing by 10.
            d = int(free % div)
            free = int(free / 10)
            keyList.append(d)
            d = 0
            div = int(div/10)
        print(rand)
        print(keyList.reverse())
        return keyList.reverse()

    # def offset():
    # def encrypt():
    if __name__ == "__main__": 
        print(key())