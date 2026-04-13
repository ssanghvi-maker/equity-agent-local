from data.sec_fetcher import get_latest_10k
from data.transcript_loader import load_transcript
from processing.cleaning import clean_text
from analysis.pipeline import run_pipeline
from output.formatter import save_output


def run_agent(cik, ticker, transcript_path):
    print(f"Running agent for {ticker}...")

    tenk = get_latest_10k(cik)
    transcript = load_transcript(transcript_path)

    tenk = clean_text(tenk)
    transcript = clean_text(transcript)

    result = run_pipeline(tenk, transcript)

    file = save_output(ticker, result)

    print(f"Saved: {file}")


if __name__ == "__main__":
    run_agent("0000320193", "AAPL", "data/aapl_transcript.txt")
