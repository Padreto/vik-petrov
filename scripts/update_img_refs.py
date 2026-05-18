import io, sys, os, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

SRC = r'C:\Users\stefan.borisov\Desktop\web\tedo-vik\src'

exts = ('.astro', '.ts', '.js', '.tsx', '.jsx', '.css')
changed_files = []

for root, dirs, files in os.walk(SRC):
    for fname in files:
        if not fname.endswith(exts):
            continue
        path = os.path.join(root, fname)
        with open(path, encoding='utf-8-sig') as f:
            content = f.read()

        # Replace .jpg and .jpeg references (in /images/ paths) with .webp
        new_content = re.sub(
            r'(/images/[^\s"\'`>)]+)\.(jpg|jpeg)',
            r'\1.webp',
            content
        )

        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            changed_files.append(path.replace(SRC, 'src'))

print(f'Updated {len(changed_files)} files:')
for f in changed_files:
    print(f'  {f}')
