block_cipher = None
a = Analysis(
    ['test_pyinstaller/__main__.py'],
     pathex=[],
     binaries=None,
     datas=None,
     hiddenimports=[],
     hookspath=[],
     runtime_hooks=None,
     excludes=["tests"],
     cipher=block_cipher
)

pyz = PYZ(
     a.pure,
     a.zipped_data,
     cipher=block_cipher
)

exe = EXE(
	pyz,
	a.scripts,
	a.binaries,
	a.zipfiles,
	a.datas,
	[],
	name='test_exec',
	debug=False,
	bootloader_ignore_signals=False,
	strip=True,
	upx=True,
	upx_exclude=[],
	runtime_tmpdir=None,
	console=True,
)
