"""
Render XML to HTML using XSLT.

Example: `python update-docs.py > media_types.html`

"""

import sys
import lxml.etree as ET

def main():
    dom = ET.parse("MediaTypes.xml")
    xslt = ET.parse("MediaTypesStyle.xsl")
    transform = ET.XSLT(xslt)
    newdom = transform(dom)
    print(ET.tostring(newdom, pretty_print=True))


if __name__ == "__main__":
    sys.exit(main())
