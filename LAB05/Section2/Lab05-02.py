price = float(input("กรุณาป้อนราคาสินค้า: "))

if price >= 100:
    vat = price * 0.07
    total_price = price + vat
    print("ยอดรวมที่ต้องชำระ (รวม VAT): {:.2f} บาท".format(total_price))
else:
    print("ยอดรวมที่ต้องชำระ: {:.2f} บาท".format(price))