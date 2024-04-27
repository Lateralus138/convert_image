#!/usr/bin/env bash
sudo apt install python3-pip -y
if [[ $? -gt 0 ]]; then
  echo "Could not install python3-pip."
  exit 1
fi
sudo apt install python3-venv -y
if [[ $? -gt 0 ]]; then
  echo "Could not install python3-venv."
  exit 2
fi
sudo apt install ccache -y
if [[ $? -gt 0 ]]; then
  echo "Could not install ccache."
  exit 3
fi
python3 -m pip install --upgrade pip
if [[ $? -gt 0 ]]; then
  echo "Could not upgrade pip - pip."
  exit 4
fi
python3 -m venv .
if [[ $? -gt 0 ]]; then
  echo "Could not create Python virtual environment."
  exit 5
fi
bin/python3 -m pip install --upgrade pip
if [[ $? -gt 0 ]]; then
  echo "Could not upgrade virtual environment pip - pip."
  exit 6
fi
bin/python3 -m pip install nuitka
if [[ $? -gt 0 ]]; then
  echo "Could not install virtual environment pip - nuitka."
  exit 7
fi
bin/python3 -m pip install Pillow
if [[ $? -gt 0 ]]; then
  echo "Could not install virtual environment pip - Pillow."
  exit 8
fi
