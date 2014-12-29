import json
import glob
if __name__ == '__main__':
    result = []
    for f in glob.glob("*.json"):
        with open(f, "rb") as infile:
            result.append(json.load(infile))
    with open("map_data.json", "wb") as outfile:
        json.dump(result, outfile)