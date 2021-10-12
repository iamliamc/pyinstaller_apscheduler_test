Create a 3.9 venv:

```
python3.9 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

```
 python -m PyInstaller pyinstaller.spec --debug=all
```

Run the executable:
`dist/.test_pyinstaller`