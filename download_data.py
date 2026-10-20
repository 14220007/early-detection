"""
Mengunduh dataset Hasan et al. (2021) dari Zenodo (record 5591907, CC BY 4.0)
ke folder tempat skrip ini berada. Jalankan sekali: python download_data.py
"""
import io
import json
import os
import urllib.request
import zipfile

RECORD = "5591907"
HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    url = f"https://zenodo.org/api/records/{RECORD}/files-archive"
    print("Mengunduh arsip dari", url, "...")
    try:
        with urllib.request.urlopen(url, timeout=300) as r:
            data = r.read()
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            z.extractall(HERE)
            print(f"Selesai: {len(z.namelist())} file diekstrak ke {HERE}")
        return
    except Exception as e:
        print("Arsip ZIP gagal diunduh (", e, "). Mencoba per file ...")

    meta = json.load(urllib.request.urlopen(f"https://zenodo.org/api/records/{RECORD}", timeout=60))
    for f in meta["files"]:
        target = os.path.join(HERE, f["key"])
        if os.path.exists(target) and os.path.getsize(target) == f["size"]:
            continue
        urllib.request.urlretrieve(f["links"]["self"], target)
        print("  ", f["key"])
    print(f"Selesai: {len(meta['files'])} file di {HERE}")


if __name__ == "__main__":
    main()
