def judge(question, expects, answer, results) -> bool:
  """
  q: 'give', expect: 'give'
  returns whether the expect is in the answer
  """

  # lower - converts string to lowercase
  # trim - strips whitespace from beginning and end
  return expects.lower().strip() in answer.lower()
  # fails if answer: '0 libraries', expects: 'no libraries', 

  # return any(expects.strip().lower() for chunk in results);

  """
  Industry practice - LLM as judge

  NLP - as judge
  Recommended: rapidfuzz - Python library for similarity scoring via natural language processing (no LLM used)
     - ex. knows that 0 libraries and no libraries semantically mean the same thing
     - Limitations: only works on small chunks - no large documents -> no vector database, distances, embeddings

  - evaluates by similarity of semantic meaning (regardless of wording), rather than directly checking
  for exact answer is in the answer
  - invoke LLM - with prompt, "judge if the expects semantically matches with the answer"
  """