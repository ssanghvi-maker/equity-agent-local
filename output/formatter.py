def save_output(ticker, text):
    filename = f"{ticker}_report.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    return filename
