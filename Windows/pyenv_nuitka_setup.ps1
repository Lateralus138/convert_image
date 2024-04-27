$py_version = ((python -V) -split '\s+', 2)[1]
if ($py_version -lt 3.8.10) {
    Write-Error "Python version < [3.8.10]"
    Exit 1
  }
python -m venv .
if ($LASTEXITCODE -gt 0) {
    Write-Error "Could not create a python virtual environment."
    Exit 2
  }
.\Scripts\python.exe -m pip install --upgrade pip
if ($LASTEXITCODE -gt 0) {
    Write-Error "Could not upgrade pip - pip."
    Exit 3
  }
.\Scripts\python.exe -m pip install nuitka
if ($LASTEXITCODE -gt 0) {
    Write-Error "Could not install pip - nuitka."
    Exit 4
  }
.\Scripts\python.exe -m pip install Pillow
if ($LASTEXITCODE -gt 0) {
    Write-Error "Could not install pip - Pillow."
    Exit 5
  }
