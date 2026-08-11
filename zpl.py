def generate_barcode_label(barcode: str) -> str:
    return f"""
^XA

^PW710
^LL203
^LH0,0

^FO180,100
^BY3,2,80
^BCN,80,N,N,N
^FD>;{barcode}^FS

^FO0,200
^A0N,36,36
^FB710,1,0,C,0
^FD{barcode}^FS

^XZ
"""