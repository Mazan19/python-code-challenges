import re

def define_palindrom(v_str):
    #print(v_str)
    v = ",./<>?-=()*:'|;&^%$#@! "

    pure = ''.join(x for x in v_str.lower() if x not in v)
    #print(pure)
    if any(not x.isalpha() for x in pure):
        return None
    
    def def_by_symbol(pure):
        len_pure = len(pure)
        for i in range(len_pure//2):
            print(f"{i} positing = {pure[i]} and {pure[len_pure-i-1]}")
            if pure[i] != pure[len_pure-i-1]:
                return False,"false"
        
        return True
    
    def def_by_slice(pure):
      #  print(f"{pure[:]} and {pure[::-1]}")
        return pure[:]==pure[::-1]

    return def_by_slice(pure)

def test(v):
    print(f"{v} is {define_palindrom(v)}")
if __name__ == "__main__":
    test("level")
    test("race car")
    test("rAcE  c A r")
    test("aaaa")
    test("aaa")
    test("its should be false")
    test("its,should,be,false")
    test("its should be none because of - and , ")
    test("Go hang a salami - I'm a lasagna hog !")