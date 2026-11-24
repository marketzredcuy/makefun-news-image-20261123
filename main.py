#!/usr/bin/env python3
"""news-image-20261123 entrypoint: copy the pre-composed front page
to the harness output directory.

The entry is a program that writes one image to /output/entry.png:
this module copies the bundled entry.png to
$MAKEFUN_OUTPUT_DIR/entry.png and verifies the copy is byte-for-byte
identical, within the size limit, square and 1024x1024.

The bundled image is a 1024x1024 newspaper front page summing up
Monday 23 November 2026 in 48 date-checked stories across 6
regions: 3 hero cards (Nvidia brings back Jensen Huang as CEO,
the EU proposes its 22nd Russia sanctions package, the US sanctions
Iran's shadow-banking network), 10 illustrated cards, a six-number
stat strip, a world map with 13 numbered dots, a two-column ALSO
list of 35 briefs, and a DATE CHECK bar that names what was left
out as other days' news. The pattern is v1 of 21 November (48
stories, dev rank 51): v2 (37 stories) scored dev rank 97 and v3
(48 stories plus date-check tags and a 9-region strip) scored dev
rank over 200, so this page goes back to the pure v1 pattern --
48 stories, a 6-region strip (no Global story survived
verification), no tags on pictured stories. Breadth won; the tags
and the extra strip cost readability.

Every story on the page was verified against Monday 23 November
reporting in three verification rounds (two independent research
passes plus own checks against Reuters, BBC and AP): the first
slates' date errors were caught before this build -- the Chapo
Isidro capture was Friday 20 Nov (only the US extradition order
is Monday's news), the Skubal-Mets $450m deal and the Democrats'
258 House seats were Sunday 22 Nov, the Dymer strike itself was
22 Nov (Monday's news is the toll rising to 11, not 15 -- 15 was
the whole Kyiv region), and the FBI NCIC hack was first reported
20 Nov. The DATE CHECK bar is honest about what was left out:
the COP31 collapse (22 Nov), the Merkury sinking (22 Nov),
Liverpool 4-0 Man United (22 Nov), the Chapo Isidro capture
(20 Nov), the Skubal-Mets deal (22 Nov), the Democrats' 258
House seats (22 Nov) and the Dymer strike itself (22 Nov).

The page was rendered from self-contained HTML with headless
Chrome over CDP and inspected twice: the first render hid the
Nvidia scene's label behind its chart arrow, clipped the EU
scene's "70+ SHIPS LISTED" line under the banner, struck the
shadow-bank scene's label through with the roofline and buried
the Bayelsa scene's caption under the banner. All four were
fixed and the second render shows all 48 stories, the DATE
CHECK bar and the footer in full.

Only the Python standard library is used. No network access.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_BYTES = 1 * 1024 * 1024
MAX_SIDE = 1024


def read_png_size(path):
    """Return the (width, height) of a PNG from its IHDR chunk.

    The PNG signature is 8 bytes; the IHDR chunk follows (4-byte
    length, 4-byte type "IHDR"), then width and height as big-endian
    uint32. Only the standard library is used.
    """
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG file")
    width = int.from_bytes(head[16:20], "big")
    height = int.from_bytes(head[20:24], "big")
    return width, height


def sha256_file(path):
    """SHA-256 of a file, streamed so a 1 MiB image stays cheap."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # shutil.copyfile is a plain byte copy: no timestamps, no
    # metadata and no randomness are written, so two runs of this
    # program produce the same bytes and the same digest.
    shutil.copyfile(src, dst)
    # The competition runs this program twice and both runs must
    # write the same bytes, so the copy must be byte-for-byte: a
    # truncated or altered copy would still pass the size checks, so
    # compare digests instead of trusting the file size alone.
    if sha256_file(src) != sha256_file(dst):
        raise SystemExit("copy mismatch: entry.png did not copy cleanly")
    size = os.path.getsize(dst)
    if size > MAX_BYTES:
        raise SystemExit(f"entry.png too large: {size} bytes (limit 1 MiB)")
    width, height = read_png_size(dst)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit(
            f"entry.png too big: {width}x{height} (limit 1024x1024)")
    if width != height:
        raise SystemExit(f"entry.png is not square: {width}x{height}")
    # The bundled image is composed at exactly 1024x1024. Anything
    # else means the bundled image was replaced, so refuse it rather
    # than submit a wrong-sized page.
    if width != MAX_SIDE or height != MAX_SIDE:
        raise SystemExit(
            f"entry.png is {width}x{height}, expected 1024x1024")
    # The bundled image is the whole entry: a zero-byte or truncated
    # copy would pass the size checks, so refuse anything implausibly
    # small as well as anything over the limit. The final image is
    # 366,624 bytes, comfortably inside the 1 MiB cap.
    if size < 100_000:
        raise SystemExit(f"entry.png implausibly small: {size} bytes")
    print(f"wrote {dst} ({size} bytes, {width}x{height}, "
          f"sha256 {sha256_file(dst)[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
