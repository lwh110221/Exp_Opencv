from PyInstaller.building.build_main import Analysis, PYZ, EXE

a = Analysis(
    ['window.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('venv/Lib/site-packages/ttkbootstrap', 'ttkbootstrap'),
        ('venv/Lib/site-packages/matplotlib', 'matplotlib'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'ttkbootstrap',
        'numpy',
        'matplotlib',
        'matplotlib.backends.backend_tkagg',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name='Lwh数字图像处理整合_Win',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='icon.ico',
    uac_admin=False,
    target_arch=None
)