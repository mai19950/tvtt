import os

def download():
  with open("./index.m3u", mode="r", encoding="utf8") as f:
    lines = f.readlines()
  lines = lines[1:]
  i, l = 0, len(lines)
  while i < l:
    title, link = lines[i : i + 2]
    title = title.strip().split(' ')[-1]
    link = link.strip()
    # print(title, link)
    os.system(rf"python E:\23_script\m3u8_download.py {title} -i {link}")
    i += 2


if __name__ == '__main__':
  download()