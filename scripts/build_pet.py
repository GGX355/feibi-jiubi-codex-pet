"""Build the Codex-compatible WebP from the editable PNG spritesheet.

Requires Pillow: python -m pip install Pillow
"""

import json
from pathlib import Path
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
PNG = ROOT / "preview" / "spritesheet.png"
PET = ROOT / "pet"
WEBP = PET / "spritesheet.webp"


def main() -> None:
    manifest = json.loads((PET / "pet.json").read_text(encoding="utf-8"))
    assert manifest["spriteVersionNumber"] == 2
    assert manifest["spritesheetPath"] == WEBP.name
    with Image.open(PNG) as source:
        atlas = source.convert("RGBA")
    assert atlas.size == (1536, 2288), atlas.size
    atlas.save(WEBP, format="WEBP", lossless=True, exact=True)
    with Image.open(WEBP) as encoded:
        assert ImageChops.difference(atlas, encoded.convert("RGBA")).getbbox() is None
    print(f"Built {WEBP} from {PNG}; RGBA pixels verified")


if __name__ == "__main__":
    main()
