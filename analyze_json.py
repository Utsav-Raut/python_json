import zipfile
import json
from pprint import pprint

class Analyze():
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def extract_Files(self):
        with zipfile.ZipFile("/home/boom/Documents/Programming/nike/archives.zip") as z:
            for filename in z.namelist():
                print(filename)
                with z.open(filename) as f:
                    data = f.read()
                    d = json.loads(data.decode("utf-8"))
                pprint(d["items"]["item"])
                batter_len = d["items"]["item"]["batters"]["batter"]
                print("Type of batter: ", len(batter_len))
                pprint(d["items"]["item"]["batters"]["batter"])


ana = Analyze("archives.zip")
ana.extract_Files()