import json

# safe dictionary as json
def safe_dict(v_dict, v_path):
    with open(v_path,'w') as output_file:
        print(json.dumps(v_dict,indent=4),file = output_file)

# load dictrionary from json
def load_dict(v_path):
    with open(v_path,'r') as input_file:
        return json.load(input_file)

v_dict = {
        "a": 123, 
        "b":"222", 
        1 : 'a',
        "dict": {
            "dict_a" : [1,2,3],
            "dict_b" : ('s,','d')
        }
}

v_path = "tmp/06_sava_dict_output.json"
safe_dict(v_dict,v_path)

loaded = load_dict(v_path)
print(json.dumps(loaded,indent=4))