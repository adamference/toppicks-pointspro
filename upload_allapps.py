import base64, os, json

folder = r'C:\Users\adamf\Desktop\Github\allapps\displayads'

files = [
    ('300x250.png', '7821', '8835', 300, 250),
    ('728x90.png', '7822', '8836', 728, 90),
    ('320x50.png', '7823', '8837', 320, 50),
    ('320x50v2.png', '7824', '8838', 320, 50),
    ('336x280.png', '7825', '8839', 336, 280),
    ('320.png', '7826', '8840', 320, 100),
]

for fname, cid, vid, w, h in files:
    path = os.path.join(folder, fname)
    with open(path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    data_uri = f'data:image/png;base64,{b64}'
    print(f'{fname} -> creative {cid}, variation {vid}, {w}x{h}, {len(data_uri)} chars')

print('\nReady for upload via MCP')
