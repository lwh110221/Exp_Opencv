from PyInstaller.building.build_main import Analysis, PYZ, EXE, BUNDLE

a = Analysis(
    ['window.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['PIL._tkinter_finder', 'ttkbootstrap'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name='Lwh数字图像处理整合_Mac',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

# 添加 BUNDLE 配置生成 .app
app = BUNDLE(
    exe,
    name='Lwh数字图像处理整合_Mac.app',
    icon='icon.icns',
    bundle_identifier='com.lwh.imageprocessor',
    info_plist={
        'CFBundleShortVersionString': '1.0.0',
        'LSMinimumSystemVersion': '10.13.0'
    }
)