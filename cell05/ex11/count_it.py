#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
    print("none")
    sys.exit(0)

print(f"parameters: {len(sys.argv) - 1}")

for param in sys.argv[1:]:
    print(f"{param}: {len(param)}")