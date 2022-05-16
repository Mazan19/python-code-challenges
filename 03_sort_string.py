import re

def sort_string(v_str):
    list_words = re.findall(r"(\w+)", v_str)
    sorted_string = ' '.join(sorted(list_words, key = str.lower))

    return sorted_string

def test(v):
    print("---------- Test results-------")
    print(f"Original is: {v}")
    print(f"Sorted is: {sort_string(v)}")


if __name__ == "__main__":
    test("String sTring of Words")
    
    test("banana ORANGE apple")
