import glob                         # thêm thư viện glob
from pathlib import Path            # thêm thư viện Path
import shutil                       # thêm thư viện sh

input_folder = "C:/Users/os/Desktop/Iot"
all_paths = glob.glob(f"{input_folder}/*")

all_ext = []

for path in all_paths:
    tmp = path.split(".")
    if len(tmp) > 1:
        all_ext.append(tmp[-1])

all_ext = list(set(all_ext))

for ext in all_ext:
    Path(f"{input_folder}/{ext}").mkdir(parents=True, exist_ok=True)

# movie file to folder
for ext in all_ext:
    files = glob.glob(f"{input_folder}/*.{ext}")
    for file_ in files:
        shutil.move(file_,f"{input_folder}/{ext}")