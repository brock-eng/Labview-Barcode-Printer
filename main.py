import os
import sys

###     Pip install list    ###
#   python-barcode
#   svglib

from barcode import Code39
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from reportlab.graphics.shapes import Drawing


def main(inputString):
    # String to print
    printableBarcode = inputString

    # Create the barcode object
    my_code = Code39(printableBarcode, add_checksum=False)

    # Saved as SVG file
    my_code.save("new_code")

    # Scale factor
    sx = 3
    sy = sx

    # Create base drawing and scale it
    drawing = svg2rlg("new_code.svg")
    drawing.scale(sx, sy)

    # Add scaled drawing to new resized file
    scaledBarcode = Drawing(drawing.width * sx, drawing.height * sy)
    scaledBarcode.add(drawing)


    # Convert to .PNG image for easy printing
    fileName = "output.png"
    renderPM.drawToFile(scaledBarcode, fileName, fmt="PNG")

    # Open file
    barcodeFilePath = "N:/ZBrock/Barcode Generator/" + fileName

    return barcodeFilePath

filepath = main(sys.argv[1])
os.startfile(filepath)
