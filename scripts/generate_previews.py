
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path.cwd()
MEDIA_DIR = ROOT / "images"
PREVIEW_DIR = MEDIA_DIR / "previews"

SUPPORTED_EXTENSIONS = {
    ".pdf", ".xlsx", ".xls", ".docx", ".doc",
    ".pptx", ".ppt", ".odt", ".ods"
}


def generate_preview(source):
    preview = PREVIEW_DIR / (source.name + ".png")
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with tempfile.TemporaryDirectory() as temp:
            temp_dir = Path(temp)

            if source.suffix.lower() == ".pdf":
                pdf_file = source
            else:
                extension = source.suffix.lower()

                if extension in {".xlsx", ".xls", ".ods"}:
                    export_filter = (
                        'pdf:calc_pdf_Export:'
                        '{"SinglePageSheets":{"type":"boolean","value":"true"}}'
                    )
                elif extension in {".docx", ".doc", ".odt"}:
                    export_filter = "pdf:writer_pdf_Export"
                elif extension in {".pptx", ".ppt"}:
                    export_filter = "pdf:impress_pdf_Export"
                else:
                    export_filter = "pdf"

                result = subprocess.run(
                    [
                        "libreoffice",
                        "--headless",
                        "--convert-to", export_filter,
                        "--outdir", str(temp_dir),
                        str(source),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=120,
                )

                pdf_file = temp_dir / (source.stem + ".pdf")

                if result.returncode != 0 or not pdf_file.exists():
                    print(f"Could not convert: {source}")
                    print(result.stderr)
                    print(result.stdout)
                    return

            output_base = temp_dir / "page"

            subprocess.run(
                [
                    "pdftoppm",
                    "-f", "1",
                    "-l", "1",
                    "-singlefile",
                    "-png",
                    "-r", "180",
                    str(pdf_file),
                    str(output_base),
                ],
                check=True,
                capture_output=True,
                timeout=120,
            )

            generated_image = temp_dir / "page.png"

            if generated_image.exists():
                shutil.copy2(generated_image, preview)
                print(f"Created preview: {preview}")
            else:
                print(f"No preview generated for: {source}")

    except Exception as error:
        print(f"Preview failed for {source}: {error}")


def main():
    if not MEDIA_DIR.exists():
        print("Images folder not found.")
        return

    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)

    for source in MEDIA_DIR.rglob("*"):
        if not source.is_file():
            continue

        if PREVIEW_DIR in source.parents:
            continue

        if source.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        generate_preview(source)


if __name__ == "__main__":
    main()
