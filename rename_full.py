"""Rename full-res originals to photo-XX.jpg without compression."""
import os
import shutil

folder = os.path.join(os.path.dirname(__file__), "images")

# Thứ tự album
mapping = [
    ("1wupukbwaag74afxbhkica6y0fsjgjyw0ajq3xfhgylknypbcio9yu3faz5nfpihblh9.jpg", "photo-01.jpg"),
    ("1wupukbwaatav9m1m9vtdgkpwir1naybxrrzfg2f8n0trxtvtkywhtijy2vpbajaxic8.jpg", "photo-02.jpg"),
    ("1wupukbwam1cakjtct6ghxyfpeolo3wwixenezujujkzixhvy4xnjaqjnpcfpd50jws11.jpg", "photo-03.jpg"),
    ("2aoboqfzrr7qp5i3tiafqyxluzrtu0fyztp8uato6.jpg", "photo-04.jpg"),
    ("2aoboqfzrpouilgqix7azr8vilb330mu4mzxizkm4.jpg", "photo-05.jpg"),
    ("1wupukbwax81vsy46kbe6cmpd84dwauvp2bmhrjdurhhxxwbisjyy6ojc4n5diosrbk1.jpg", "photo-06.jpg"),
    ("2aoboqfzsesisama7x5upzasmmtnmlpnicbwtyoc13.jpg", "photo-07.jpg"),
    ("1wupukbwan4xvzimrv5dikj2upnztthaiyo6z74icjymfgfnpkjafzjqze5epjsj2ef14.jpg", "photo-08.jpg"),
    ("1wupukbwaxoezbepkwayrbe0pszvdkivpolvohzedecj8okcpfzoatzgq54komrzp1d2.jpg", "photo-09.jpg"),
    ("1wupukbwalbd5ssxwbi85fxnrdjzzkik8ioazmajevk9ead1fxkbk2otgz7dswxxa5i10.jpg", "photo-10.jpg"),
    ("1wupukbwamje8e42lv2kfb4tgsxsrzrqqrcj11xcw3rg5acaiqhvcafwmdze7oeifdf12.jpg", "photo-11.jpg"),
    ("2aoboqfzrowtpgyauh3brc3h433scanhljc5hq2y3.jpg", "photo-12.jpg"),
    ("2aoboqfzrqotowznb27qkpwnnklgctkzo7nojgaq5.jpg", "photo-13.jpg"),
    ("2aoboqfzrrkl9pumv1j69so8m3w2jcvptk0zxxzy7.jpg", "photo-14.jpg"),
]

found = 0
for src_name, dst_name in mapping:
    src = os.path.join(folder, src_name)
    dst = os.path.join(folder, dst_name)
    if not os.path.exists(src):
        continue
    shutil.copy2(src, dst)
    os.remove(src)
    found += 1
    print(f"OK  {dst_name}  ({os.path.getsize(dst) // 1024} KB, giữ nguyên chất lượng)")

if found == 0:
    print("Không tìm thấy file gốc (tên hash). Hãy copy 14 ảnh gốc vào thư mục images/ rồi chạy lại.")
elif found < 14:
    print(f"\nĐã rename {found}/14 ảnh. Thiếu {14 - found} file — copy thêm rồi chạy lại.")
else:
    total = sum(
        os.path.getsize(os.path.join(folder, f))
        for f in os.listdir(folder)
        if f.lower().endswith(".jpg")
    )
    print(f"\nXong! Tổng: {total / 1024 / 1024:.2f} MB")
