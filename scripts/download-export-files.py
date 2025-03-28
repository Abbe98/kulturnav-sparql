import urllib.request
import os

def download_file(url, filename):
    headers = {
        "User-Agent": "FornPunkt SPARQL Updater/0.1",
    }
    request = urllib.request.Request(url, headers=headers)

    print(f"Downloading {filename} from {url}")
    with urllib.request.urlopen(request) as response:
        with open(filename, "wb") as f:
            f.write(response.read())


for file in os.listdir("."):
    if file.endswith(".rdf"):
        os.remove(file)

files = {
    "arkitekter.rdf": "https://kulturnav.org/exportRdfxml/search/entity.dataset:2b7670e1-b44e-4064-817d-27834b03067c/0/10000", # Arkitekter verksamma i Sverige
    "byggnader.rdf": "https://kulturnav.org/exportRdfxml/search/entity.dataset:1f23ddae-5579-4e3e-bf59-a29524e4f926/0/10000" # Byggnader i Sverige
}

for file, url in files.items():
    download_file(url, file)
