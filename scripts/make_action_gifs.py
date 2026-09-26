"""Rebuild nine GIFs and browser frames from the released atlas (Pillow)."""
import json
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'preview'
def main():
    atlas = Image.open(OUT / 'spritesheet.png').convert('RGBA')
    assert atlas.size == (1536,2288)
    actions = json.loads((OUT/'actions.json').read_text(encoding='utf-8'))
    assert [a['row'] for a in actions] == list(range(9))
    assert [len(a['times']) for a in actions] == [6,8,8,4,5,8,6,6,6]
    assets = OUT/'assets'
    assets.mkdir(exist_ok=True)
    for row,count in enumerate([6,8,8,4,5,8,6,6,6,8,8]):
        for col in range(count):
            atlas.crop((col*192,row*208,(col+1)*192,(row+1)*208)).save(assets/f'{row}-{col}.png')
    for action in actions:
        frames=[]
        for col in range(len(action['times'])):
            sprite=Image.open(assets/f"{action['row']}-{col}.png").convert('RGBA')
            frame=Image.new('RGBA',(192,208),'#fffaf0')
            frame.alpha_composite(sprite)
            frames.append(frame.convert('RGB').resize((384,416),Image.Resampling.LANCZOS))
        sheet=Image.new('RGB',(384,416*len(frames)))
        for i,frame in enumerate(frames):sheet.paste(frame,(0,416*i))
        palette=sheet.quantize(colors=224)
        indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
        dest=OUT/f"{action['id']}.gif"
        indexed[0].save(dest,save_all=True,append_images=indexed[1:],duration=action['times'],loop=0,disposal=2,optimize=False)
        with Image.open(dest) as check:
            assert check.n_frames==len(frames)
            durations=[]
            for i in range(check.n_frames):
                check.seek(i)
                durations.append(check.info['duration'])
            assert durations==action['times']
        print(f'Built and verified {dest.name}')
    (OUT/'actions.js').write_text('const PET_ACTIONS = '+json.dumps(actions,ensure_ascii=False,indent=2)+';',encoding='utf-8')
if __name__=='__main__':main()
