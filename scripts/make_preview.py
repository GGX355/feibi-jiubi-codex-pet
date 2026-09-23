"""Render a compact preview from the released, editable PNG atlas.

Requires Pillow: python -m pip install Pillow
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ATLAS = Image.open(ROOT / "preview" / "spritesheet.png").convert("RGBA")
OUT = ROOT / "preview"
CELL_W, CELL_H = 192, 208


def cell(row: int, column: int) -> Image.Image:
    return ATLAS.crop(
        (column * CELL_W, row * CELL_H, (column + 1) * CELL_W, (row + 1) * CELL_H)
    )


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in (
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ):
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def main() -> None:
    assert ATLAS.size == (8 * CELL_W, 11 * CELL_H)
    board = Image.new("RGB", (1300, 650), "#f8f5fa")
    draw = ImageDraw.Draw(board)
    draw.text((72, 38), "PHOEBE JIUBI", font=font(42), fill="#3c304c")
    draw.text((72, 103), "Codex pet · fan-made animation preview", font=font(22), fill="#826f98")
    poses = [(0, 0, "Idle"), (3, 1, "Wave"), (4, 2, "Jump")]
    for i, (row, column, label) in enumerate(poses):
        x = 65 + i * 410
        draw.rounded_rectangle((x, 177, x + 350, 570), radius=28, fill="#fffaf0")
        sprite = cell(row, column).resize((288, 312), Image.Resampling.LANCZOS)
        board.paste(sprite, (x + 31, 203), sprite)
        draw.text((x + 138, 528), label, font=font(20), fill="#6c597f")
    board.save(OUT / "cover.png")


if __name__ == "__main__":
    main()
