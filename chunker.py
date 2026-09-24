"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    
    # number of characters duplicated in adjacent chunks (if exists)
    overlap = overlap or config.CHUNK_OVERLAP 

    if overlap >= chunk_size: # means you have identical chunks
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0 # position in document text
        index = 0 # chunk #
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece: # append if slice (chunk) isn't empty
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap  # advance start(ing point) by less than chunk size so next chunk has overlap

    return chunks


def split_by_replies(documents: list[Document]) -> list[Chunk]:
    """Split each thread into one chunk per reply
       - splits by paragraph break (new line)
       - removes document header and reply headers
    """
    chunks: list[Chunk] = []

    reply_pattern = re.compile(
        r"(?ms)^\s*---\s*reply\s+\d+\s*(?:\([^)]*\))?\s*---\s*\n*(.*?)(?=^\s*---\s*reply\s+\d+\s*(?:\([^)]*\))?\s*---\s*|\Z)"
    )

    for doc in documents:
        for index, match in enumerate(reply_pattern.finditer(doc.text)):
            piece = match.group(1).strip()
            if not piece:
                continue
            chunks.append(
                Chunk(
                    text=piece,
                    source=doc.source,
                    index=index,   # document-specific chunk # (not chunk # in full corpus)
                    produced_by="chunker.py::split_documents",
                )
            )

    return chunks


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split documents into chunks. ⚠️ REPLACE THE BODY OF THIS IN MILESTONE 3.

    Right now it just calls the fallback. That is the plain, generic behaviour
    the brief is talking about.

    When you write your own strategy, set `produced_by` to
    "chunker.py::split_documents" so your README's Sample Chunks section names
    the right function. `app.py chunks` prints that string for you.

    Things worth thinking about before you write any code:
      - Are your documents short posts or long guides?
      - Is the useful information in one sentence, or spread over a paragraph?
      - Would splitting on paragraph breaks keep more thoughts intact than
        splitting on a character count?
    """
    return split_by_replies(documents)
    # return fallback_split(documents)

    # chunk 2, 8, 15 = not good - can't stand alone, too short

    # issue with current chunking approach
    # """
    # python app.py index
    # corpus: advice_threads, format = short threads
    #     loaded   23 documents, 12,490 characters, ~543 characters per document
    #     chunked  26 chunks, 487 characters on average (shortest 2, longest 793), produced by chunker.py::fallback_split
    
    # # ****python app.py chunks -n 26 (bc python app.py index = 26 chunks by default for advice_threads)
    # # - use to show all chunks
        
    # current approach: fixed-size chunking, chunk_size = 800, overlap = 200 -> 600 new chars
    # - chunked by DOCUMENT
    # - issue: if 2nd to last chunk in current doc has <800 chars total
    #   - next start = prev start + 800 - 200 (shift by 600)
    #   - may end up with fragmented chunks that clip whatever remains in frame at end of 2nd to last chunk
    #       "ex. 
    # """





    # goal:
    # """
    # Since I"m using advice_threads, which has short 2-3 sentence replies.

    # I will use each reply as a chunk - this guarantees that each chunk contributes 1 key topic (and possibly some supporting, but to make that topic stronger).
    # - Each reply can stand alone (is a complete thought)
    # - Doesn't run the risk of multiple replies introducing different ideas
    # aka. split on PARAGRAPH BREAKS > character count (each brief paragraph = complete idea), each reply is an individual/standalone idea, even if related
    # 
    # criteria - good chunk: complete, standalone + focused thought
    # ex. "Professor Smith's exams come from the lecture slides, not the textbook. Students say attending every class matters more than doing the readings. Midterms are curved; finals are not."
    # - incomplete - no a full standalone thought
    # ex. "Professor Smith's exams come from the"
    # - too big - 4 topics, every matches every question a little and no question well
    #
    #
    # result:
    # Corpus: advice_threads - 75 chunks
    #   loaded   23 documents, 12,490 characters, ~543 characters per document
    #   chunked  75 chunks, 121 characters on average (shortest 68, longest 195), produced by chunker.py::split_documents
    # """




    # testing (running eval)
    # """
    # python run_eval.py --label before
    # """

    # # improvements/next steps
    # """
    # During loading phase:
    # - clean (remove) forum headers in `ingest.py`
    # - since these are all questions - shouldn't be used as a chunk retrieved for generating answers

    # "is it a good idea in chunking to delete parts? ex. I know that every thread in advice_threads starts with THREAD:

    # and that isn't useful answer - it's alwayas a q

    # should chunking part be doing any claening, or shoudl that be reserved for the loading part
    # "
    # """

def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
