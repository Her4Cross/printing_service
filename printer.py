import os
import socket
from dotenv import load_dotenv

from zpl import generate_barcode_label

load_dotenv()

PRINTER_IP = os.getenv("ZEBRA_HOST")
PRINTER_PORT = int(os.getenv("ZEBRA_PORT", "9100"))


def send_to_printer(zpl: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((PRINTER_IP, PRINTER_PORT))
        s.sendall(zpl.encode("utf-8"))


def print_items(items):

    for item in items:

        zpl = generate_barcode_label(item.barcode)

        for _ in range(item.quantity):
            send_to_printer(zpl)