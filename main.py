import pathlib
import shutil

src = pathlib.Path(__file__).parent / "entry.png"
dst = pathlib.Path("/output/entry.png")
dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(src, dst)
