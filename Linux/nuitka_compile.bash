#!/usr/bin/env bash
bin/python3 -m nuitka --standalone --onefile \
  --company-name="New Pride Software/Services" \
  --product-name="Convert Image" \
  --file-version=1 \
  --product-version=1 \
  --file-description="Image conversion using Pillow." \
  --copyright="© 2024 Ian Pride" \
  "./src/convert_image.py"
