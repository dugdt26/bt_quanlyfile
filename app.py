import glob                         # thêm thư viện glob
from pathlib import Path            # thêm thư viện Path
import shutil                       # thêm thư viện sh
import os

input_folder = "C:/Users/os/Desktop/Iot"
all_folder = glob.glob(f"{input_folder}/*")     # truy nhập vào đường link và tạo ra một list string .
all_ext= []
for path in all_folder:
    if os.path.isdir(path):                     # kiểm xem các phần tử bên trong all_folder có phải là các đường dẫn hiện có hay là ko.
        all_ext.append(path.split("/")[-1])     # biến các đường link thành 1 list phân biệt bởi "/" sau đó lấy phân tử [-1] cho vào all_ext.

print(all_ext)

all_ext = list(set(all_ext))                    # lấy các phần tử không trùng lặp tạo thành 1 list.

# movie file to folder
for ext in all_ext:
    files = glob.glob(f"{input_folder}/{ext}/*")
    for file_ in files:
        filename_ext = os.path.basename(file_)
        print(filename_ext)
        filename = filename_ext.split(f".{ext}")[0]
        size = Path(file_).stat().st_size
        os.rename(file_, f"{input_folder}/{ext}/{filename}_{size}.{ext}")