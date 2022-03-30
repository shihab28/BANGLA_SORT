# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['BANGLA_QA_PASS.py'],
             pathex=[(r'C:\Users\dtco-gf\Desktop\AUTOMATION_TEAM\BANGLA_SORT\resource', '.'), 
             ('C:\Users\dtco-gf\Desktop\AUTOMATION_TEAM\BANGLA_SORT\font', '.')],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='BANGLA_QA_PASS',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='BANGLA_QA_PASS')
