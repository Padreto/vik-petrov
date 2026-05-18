import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from PIL import Image

BASE = r'C:\Users\stefan.borisov\Desktop\web\tedo-vik\public\images'

# Max dimensions per image type
SIZES = {
    'hero-bg': (1920, 1080),
    'default': (1200, 900),
}

def get_max_size(name):
    if 'hero' in name:
        return SIZES['hero-bg']
    return SIZES['default']

total_before = 0
total_after = 0
converted = []

for root, dirs, files in os.walk(BASE):
    for fname in files:
        if not fname.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            continue
        src_path = os.path.join(root, fname)
        stem = os.path.splitext(fname)[0]
        dst_path = os.path.join(root, stem + '.webp')

        size_before = os.path.getsize(src_path)
        total_before += size_before

        try:
            with Image.open(src_path) as img:
                # Convert RGBA/P to RGB for JPEG-type WebP
                if img.mode in ('RGBA', 'P', 'LA'):
                    img = img.convert('RGBA')
                else:
                    img = img.convert('RGB')

                # Resize if too large
                max_w, max_h = get_max_size(stem)
                if img.width > max_w or img.height > max_h:
                    img.thumbnail((max_w, max_h), Image.LANCZOS)

                # Save as WebP
                img.save(dst_path, 'WEBP', quality=82, method=6)

            size_after = os.path.getsize(dst_path)
            total_after += size_after
            ratio = (1 - size_after / size_before) * 100

            # Remove original only if it's not already webp
            if not fname.lower().endswith('.webp'):
                os.remove(src_path)
                converted.append(f'  {fname} → {stem}.webp  ({size_before//1024}KB → {size_after//1024}KB, -{ratio:.0f}%)')
            else:
                # Already webp — just overwrite (already done by saving to dst_path)
                converted.append(f'  {fname} (re-optimized)  ({size_before//1024}KB → {size_after//1024}KB, -{ratio:.0f}%)')

        except Exception as e:
            print(f'  ERROR {fname}: {e}')

print(f'Converted {len(converted)} images:')
for line in converted:
    print(line)
print(f'\nTotal before: {total_before//1024} KB')
print(f'Total after:  {total_after//1024} KB')
print(f'Saved: {(total_before-total_after)//1024} KB ({(1-total_after/total_before)*100:.0f}% reduction)')
