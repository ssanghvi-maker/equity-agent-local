from processing.chunking import chunk_text
from analysis.llm_local import run_llm
from analysis.prompts import *


def analyze(text, prompt):
    chunks = chunk_text(text)
    outputs = []

    for chunk in chunks:
        outputs.append(run_llm(prompt, chunk))

    return "\n".join(outputs)


def run_pipeline(tenk, transcript):
    print("Analyzing 10-K...")
    tenk_notes = analyze(tenk, TENK_PROMPT)

    print("Analyzing Transcript...")
    transcript_notes = analyze(transcript, TRANSCRIPT_PROMPT)

    print("Behavior analysis...")
    behavior = run_llm(BEHAVIOR_PROMPT, transcript_notes)

    print("Hedge fund layer...")
    hf = run_llm(HEDGE_FUND_PROMPT, tenk_notes + transcript_notes)

    print("Final memo...")
    final = run_llm(FINAL_PROMPT, tenk_notes + transcript_notes + behavior + hf)

    return final
