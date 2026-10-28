# Historical system verification: preparation

Neither Owens's complete system nor Nielsen's complete system is available in this branch. No congruence count, lcm, timing or historical-system verdict is reported.

The replay harness takes explicit checker paths, so the independently authored checkers in PR #7 can be tested without duplicating or modifying their source. It records input and checker hashes, exact commands, stdout, stderr, exit status and elapsed time. A timeout, resource cap, parse error, rejection or disagreement remains unresolved.

Run `python3 tools/replay_both.py systems/owens-42.txt PATH_TO_FIRST_CHECKER PATH_TO_SECOND_CHECKER --output replay.json`. Preserve the transcription headers and separately report the congruence count and exact lcm. A bounded checker may be unable to decide a record-size lcm; a resource error is not a mathematical counterexample.

Acceptance requires both historical transcriptions, independent source comparison, successful replay evidence and a signed human review before external reporting. Synthetic runner fixtures verify the harness, not either historical covering claim.
