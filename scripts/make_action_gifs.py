"""Build the three README animations from the released spritesheet.

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

# Match the frame order and approximate playback timing of Codex pet v2.
ACTIONS = {
    "run-left.gif": (2, 8, 120, 220),
    "jump.gif": (4, 5, 140, 280),
    "working.gif": (7, 6, 120, 220),
}


def build(name: str, row: int, count: int, frame_ms: int, last_ms: int) -> None:
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
        duration=[frame_ms] * (count - 1) + [last_ms],
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
