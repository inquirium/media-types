"""
Generate full fourcc entry based on four-char string.

The table includes the little-endian hex representation of the
four-char string. This utility spits out the complete entry
when passed the shorter string.

Example:

```
$python fourcc.py "TEXT"
0x54584554 ('TEXT')
```

"""

import sys


def le_hex_string(fourcc):
    """Generate the little-endian hex representation."""
    values = [
        f"{ord(ch):02X}"
        for ch in fourcc
    ]
    values.reverse()
    return "".join(values)


def main():
    args = sys.argv[1:]
    if len(args) < 1:
        print("fourcc.py FOURCC")
        exit()

    fourcc = args[0]
    if len(fourcc) != 4:
        print("FOURCC length must be 4")
        exit()

    print(f"0x{le_hex_string(fourcc)} ('{fourcc}')")


if __name__ == "__main__":
    sys.exit(main())
