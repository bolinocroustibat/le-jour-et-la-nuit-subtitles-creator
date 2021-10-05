import csv
import io
import urllib

from googletrans import Translator
import typer

from config import *


app = typer.Typer()


@app.command()
def create_subtitles(lang: str) -> None:

    # # Display the available languages
    # import googletrans
    # typer.secho(f"Available languages: {googletrans.LANGUAGES}", fg=typer.colors.YELLOW)

    output_path: str = f"{OUTPUT_FILENAME}_{lang.upper()}.srt"

    with open(output_path, "w+") as output_file:

        if lang != "fr":
            translator = Translator()

        try:
            typer.secho("Reading from online CSV Google Doc.", fg=typer.colors.MAGENTA)
            # Try to read from the online Google Doc
            webpage = urllib.request.urlopen(SOURCE_CSV_URL)
            reader = csv.reader(io.TextIOWrapper(webpage))
        except:
            typer.secho(
                f"Reading from local CSV {SOURCE_CSV_LOCAL_PATH}.",
                fg=typer.colors.MAGENTA,
            )
            reader = csv.reader(open(SOURCE_CSV_LOCAL_PATH, encoding="utf-8"))

        next(reader)  # Skip first line

        for count, row in enumerate(reader):

            typer.secho(f"Reading line {count}...", fg=typer.colors.BLUE)

            starttime: str = row[0]
            endtime: str = row[1]
            text: str = row[2]

            if lang != "fr":
                result = translator.translate(text, src="fr", dest=lang)
                text = result.text

            typer.secho(text, fg=typer.colors.CYAN)

            output_file.write(f"{count}\n{starttime} --> {endtime}\n{text}\n\n")

        typer.secho(
            f"\nSubtitles successfully created in {output_path}.", fg=typer.colors.GREEN
        )


if __name__ == "__main__":
    app()
