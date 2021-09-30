import csv
import io
import urllib

from googletrans import Translator
import typer


app = typer.Typer()


# SOURCE_FILE_PATH = "source_data/source.csv"
SOURCE_FILE_PATH = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT2NdoQUO3_O--eDbcysyt0ePmJ3MnCmQoOAffhVC3zT-U28_XkvD0iEJ1W_-oQB2uh7axRnVGtXALD/pub?output=csv"
# OUTPUT_FILENAME = "export_data/le_jour_et_la_nuit"
OUTPUT_FILENAME = "/Users/bolino/Google Drive/My Drive/MOVIES/Le jour et la nuit (1997)/Le Jour Et La Nuit (1997) Bernard-Henri Lévy - Alain Delon, Lauren Bacall, Arielle Dombasle (French)"
SOURCE_LANG = 'fr'


@app.command()
def create_subtitles(lang: str) -> None:

    # # Display the available languages
    # import googletrans
    # typer.secho(f"Available languages: {googletrans.LANGUAGES}", fg=typer.colors.YELLOW)

    output_path: str = f"{OUTPUT_FILENAME}_{lang.upper()}.srt"

    with open(output_path, "w+") as output_file:

        if lang != SOURCE_LANG:
            translator = Translator()

        # If source CSV is online Google Doc
        webpage = urllib.request.urlopen(SOURCE_FILE_PATH)
        reader = csv.reader(io.TextIOWrapper(webpage))
        
        # # If source CSV is local file
        # reader = csv.reader(open(SOURCE_FILE_PATH, encoding="utf-8"))

        next(reader)  # Skip first line

        for count, row in enumerate(reader):

            typer.secho(f"Reading line {count}...", fg=typer.colors.BLUE)

            starttime: str = row[0]
            endtime: str = row[1]
            text: str = row[2]
            
            if lang != SOURCE_LANG:
                result = translator.translate(text, src=SOURCE_LANG, dest=lang)
                text = result.text

            typer.secho(text, fg=typer.colors.CYAN)

            output_file.write(f"{count}\n{starttime} --> {endtime}\n{text}\n\n")

        typer.secho(f"\nSubtitles successfully created in {output_path}.", fg=typer.colors.GREEN)


if __name__ == "__main__":
    app()
