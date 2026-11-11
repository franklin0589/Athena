python -m venv .venv
.\.venv\Scripts\activate
pip install --upgrade build setuptools[core] pyinstaller
python -m build
# pyinstaller --onefile src/{package_name}/__main__.py
