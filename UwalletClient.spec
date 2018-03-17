# -*- mode: python -*-

block_cipher = None


a = Analysis(['UwalletClient.py'],
             pathex=['F:\\MyProject\\Ulord\\uwallet-client'],
             binaries=[],
             datas=[('uwallet/wordlist', 'uwallet/wordlist')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='UwalletClient',
          debug=False,
          strip=False,
          upx=True,
          console=True , version='UwalletClient.txt', icon='BwalletClient.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='UwalletClient')
