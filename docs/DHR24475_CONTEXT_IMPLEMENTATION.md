# Pre-count implementation clarification

This clarification was saved before the first corpus context-screen run.
The frozen design remains unchanged. In addition to000, the implementation
excludes999 from known matching tokens and retains eligible four-cell cases in
the uncertainty ledger. This is a conservative representation decision: the
existing corpus parser (`scripts/prepare_corpora.py`, parse_lipi) already labels
both000 and999 as unknown/separator tokens. This does not assign999 a sign
meaning or settle its exact source notation. It prevents a separator from
becoming an apparent known-sign substitution.

The six synthetic matcher tests were run before corpus counts. They check all
81 length-four strings over a three-code alphabet against a direct Hamming
oracle, slash uncertainty, multi-alternative incompatibility, leading zeros,
reversal/substring/length false matches and damaged/unknown syntax. Primary,
boundary and slash branches will remain separate as specified in the protocol.
