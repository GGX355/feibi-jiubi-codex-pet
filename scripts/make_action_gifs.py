"""Build all nine standard-action GIFs from the released spritesheet.

Requires Pillow: python -m pip install Pillow
"""

from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ATLAS = Image.open(ROOT / "preview" / "spritesheet.png").convert("RGBA")
OUT = ROOT / "preview"
CELL = (192, 208)
SIZE = (384, 416)
BACKGROUND = "#fffaf0"

# Rows 0-8 are the standard Codex pet actions. Durations are in milliseconds.
ACTIONS = {
    "idle.gif": (0, [520, 100, 90, 100, 160, 530]),
    "run-right.gif": (1, [120] * 7 + [220]),
    "run-left.gif": (2, [120] * 7 + [220]),
    "waving.gif": (3, [190] * 3 + [280]),
    "jump.gif": (4, [140] * 4 + [280]),
    "failed.gif": (5, [190] * 7 + [280]),
    "waiting.gif": (6, [200] * 5 + [300]),
    "working.gif": (7, [120] * 5 + [220]),
    "review.gif": (8, [200] * 5 + [300]),
}


def build(name: str, row: int, durations: list[int]) -> None:
    count = len(durations)
    frames = []
    for col in range(count):
        rect = (col * CELL[0], row * CELL[1], (col + 1) * CELL[0], (row + 1) * CELL[1])
        sprite = ATLAS.crop(rect)
        frame = Image.new("RGBA", CELL, BACKGROUND)
        frame.alpha_composite(sprite)
        frames.append(frame.convert("RGB").resize(SIZE, Image.Resampling.LANCZOS))

    # One shared palette avoids a color shift as the GIF changes frames.
    palette_sheet = Image.new("RGB", (SIZE[0], SIZE[1] * count), BACKGROUND)
    for index, frame in enumerate(frames):
        palette_sheet.paste(frame, (0, SIZE[1] * index))
    palette = palette_sheet.quantize(colors=224)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(
        OUT / name,
        save_all=True,
        append_images=indexed[1:],
        duration=durations,
        loop=0,
        disposal=2,
        optimize=False,
    )


def main() -> None:
    assert ATLAS.size == (CELL[0] * 8, CELL[1] * 11)
    for filename, args in ACTIONS.items():
        build(filename, *args)
        print(f"Built {OUT / filename}")


if __name__ == "__main__":
    main()
