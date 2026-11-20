import base64
import os
from PIL import Image
import numpy as np

src_path = r'C:\Users\HP\.gemini\antigravity\brain\fa9b8edc-df5b-430c-863f-1cdf4f144177\.user_uploaded\media_1795154793867_c12b010a.png'
img = Image.open(src_path).convert('RGBA')

os.makedirs('web/assets', exist_ok=True)
os.makedirs('freevideo_engine/assets', exist_ok=True)
os.makedirs('docs/assets', exist_ok=True)

# 1. Tight crop of full logo with small padding: (120, 75, 905, 275)
crop_full = img.crop((120, 75, 905, 275))
crop_full.save('web/assets/gryvids.png', 'PNG')
crop_full.save('web/assets/gryvids-dark.png', 'PNG')
crop_full.save('freevideo_engine/assets/gryvids.png', 'PNG')
crop_full.save('docs/assets/gryvids.png', 'PNG')
print('Saved web/assets/gryvids.png', crop_full.size)

# 2. Light theme version (dark text)
arr = np.array(crop_full)
arr_light = arr.copy()
for y in range(arr_light.shape[0]):
    for x in range(200, arr_light.shape[1]):
        r, g, b, a = arr_light[y, x]
        if a > 20:
            if r > 180 and g > 180 and b > 180:
                arr_light[y, x, 0] = 26
                arr_light[y, x, 1] = 31
                arr_light[y, x, 2] = 44
img_light = Image.fromarray(arr_light, 'RGBA')
img_light.save('web/assets/gryvids-light.png', 'PNG')
print('Saved web/assets/gryvids-light.png')

# 3. Wordmarks for launcher
wm = crop_full.copy()
wm.thumbnail((456, 76), Image.Resampling.LANCZOS)
wm_canvas = Image.new('RGBA', (456, 76), (0, 0, 0, 0))
wm_x = (456 - wm.width) // 2
wm_y = (76 - wm.height) // 2
wm_canvas.paste(wm, (wm_x, wm_y), wm)
wm_canvas.save('freevideo_engine/assets/wordmark.png', 'PNG')

wm2 = crop_full.copy()
wm2.thumbnail((912, 152), Image.Resampling.LANCZOS)
wm2_canvas = Image.new('RGBA', (912, 152), (0, 0, 0, 0))
wm2_x = (912 - wm2.width) // 2
wm2_y = (152 - wm2.height) // 2
wm2_canvas.paste(wm2, (wm2_x, wm2_y), wm2)
wm2_canvas.save('freevideo_engine/assets/wordmark@2x.png', 'PNG')
print('Saved wordmarks')

# 4. G icon 512x512
icon_raw = img.crop((126, 82, 327, 266))
icon_512 = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
icon_scaled = icon_raw.copy()
icon_scaled.thumbnail((400, 400), Image.Resampling.LANCZOS)
ix = (512 - icon_scaled.width) // 2
iy = (512 - icon_scaled.height) // 2
icon_512.paste(icon_scaled, (ix, iy), icon_scaled)
icon_512.save('web/assets/icon.png', 'PNG')
icon_512.save('freevideo_engine/assets/icon.png', 'PNG')
icon_512.save('docs/assets/icon.png', 'PNG')
print('Saved icon.png')

# 5. Multi-res .ico
icon_512.save('freevideo_engine/assets/icon.ico', format='ICO', sizes=[(16,16), (24,24), (32,32), (48,48), (64,64), (128,128), (256,256)])
print('Saved icon.ico')

# 6. SVGs with embedded base64 PNG
def make_svg(png_path, width, height):
    with open(png_path, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="GryVids">
  <title>GryVids</title>
  <image href="data:image/png;base64,{b64}" x="0" y="0" width="{width}" height="{height}" />
</svg>'''

svg_dark = make_svg('web/assets/gryvids.png', crop_full.width, crop_full.height)
with open('web/assets/freevideo.svg', 'w', encoding='utf-8') as f:
    f.write(svg_dark)
with open('web/assets/gryvids.svg', 'w', encoding='utf-8') as f:
    f.write(svg_dark)

svg_light = make_svg('web/assets/gryvids-light.png', crop_full.width, crop_full.height)
with open('web/assets/freevideo-light.svg', 'w', encoding='utf-8') as f:
    f.write(svg_light)
with open('web/assets/gryvids-light.svg', 'w', encoding='utf-8') as f:
    f.write(svg_light)

svg_icon = make_svg('web/assets/icon.png', 512, 512)
with open('web/assets/icon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_icon)
print('Generated SVGs successfully!')
