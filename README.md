# covering-min-modulus

**Does the record covering system with minimum modulus 42 check out, and is there one with minimum modulus 43?**

A covering system is a finite list of congruences, such as "n is even" and "n leaves remainder 1 when divided by 3",
chosen so that every integer satisfies at least one of them. In each congruence, the number you divide by is its
modulus. In Erdős's problem the moduli must all be different. For example, every integer is even, or a multiple
of 3, or leaves remainder 1 when divided by 4, remainder 5 when divided by 6, or remainder 7 when divided by 12. The
smallest modulus of that system is 2.

Erdős asked whether the smallest modulus can be made as large as you like. Hough proved in 2015 that it cannot.
Balister and others gave a simpler proof in 2022 and showed that the smallest modulus is at most 616,000. The best
construction known has smallest modulus 42, from Tyler Owens's 2014 master's thesis. This project re-checks that
record independently and searches for a system with smallest modulus 43.

Part of Foundation0's mathematics work ([math0](https://github.com/Foundation-0/math0)). It began in Foundation0's
[deep-fields scouting](https://github.com/Foundation-0/f0/tree/main/deep-fields) of 18–19 October 2026.

**Status: not started.**

## What is known

Checked against the sources on 19 Oct 2026:

- [Erdős problem 2](https://www.erdosproblems.com/2) says: "The best known lower bound is a covering system with
  minimum modulus 42, due to Owens [Ow14]". Balister et al. [BBMST22] "improved the upper bound on the smallest
  modulus to 616000". The same page credits Hough [Ho15] with the first proof that the answer is no, with a bound of
  10<sup>16</sup>.
- The record comes from Tyler Owens, "A Covering System with Minimum Modulus 42", MS thesis, Brigham Young
  University, December 2014 ([BYU ScholarsArchive](https://scholarsarchive.byu.edu/etd/4329)).
- Nielsen's system with smallest modulus 40 is in Pace P. Nielsen, "A covering system whose smallest modulus is
  40", Journal of Number Theory 129 (2009), 640–666
  ([doi:10.1016/j.jnt.2008.09.016](https://doi.org/10.1016/j.jnt.2008.09.016)).
- Google DeepMind's formal-conjectures, a collection of open problems stated in Lean,
  [states the problem](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/2.lean)
  for distinct covering systems, where all moduli are different.

From the scouting report, not yet re-checked:

- No journal version of the thesis and no independent verification of 42 were found.
- One paper marks the attribution to Owens "(???)" ([arXiv:1905.07386](https://arxiv.org/abs/1905.07386)). A 2024
  paper cites 42 ([arXiv:2407.15280](https://arxiv.org/abs/2407.15280)).
- The previous record was Nielsen's 40 (2009).
- BYU's site blocked automated download of the thesis, so a person may need to download the PDF.

The full notes are in [notes/scouting-2026-10-19.md](notes/scouting-2026-10-19.md).

## Who else is working on this

The scouting found no independent check of Owens's 42 (not yet re-checked). On 19 Oct 2026 the problem's page on
erdosproblems.com listed one forum user as working on the problem and one as formalising it.

## How a result is checked

The certificate is the list of congruences itself, so anyone can check it. A list covers every integer exactly when
it covers every remainder on division by the lcm, the least common multiple of all the moduli, because the pattern
repeats with that period. For record systems the lcm is too large to try every remainder. A checker can work through
the lcm's prime factors instead, using the Chinese remainder theorem: a remainder on division by a product of numbers
with no common factor is the same as one remainder for each of them.

A result counts when two programs that share no code agree on it. A checker verified in Lean, a proof checker, is
possible later. If Owens's 42 turns out wrong, that is itself a result. A system with smallest modulus 43 may need an
lcm far beyond reach.

## How to contribute

The lead is to be named, and a person signs for every result.

- People and agents: read [AGENTS.md](AGENTS.md), then pick an
  [open issue](https://github.com/Foundation-0/covering-min-modulus/issues).
- New to Foundation0: start with [JOIN.md](https://github.com/Foundation-0/f0/blob/main/JOIN.md).
- Agents split up and hand off work in [st0a](https://github.com/Foundation-0/st0a). Questions and ideas go to the
  [forum](https://github.com/Foundation-0/f0/discussions).

## Files

| path | what |
|---|---|
| [`AGENTS.md`](AGENTS.md) | the guide for AI agents, which [`CLAUDE.md`](CLAUDE.md) loads for Claude Code |
| [`notes/scouting-2026-10-19.md`](notes/scouting-2026-10-19.md) | the research so far, with every source |
| [`notes/reports/`](notes/reports/README.md) | the complete scouting reports, kept as written, and the fact-check |
| [`systems/README.md`](systems/README.md) | the file format for a covering system |
| [`.github/`](.github/) | the pull request template and the task form |

## Licence

Apache License 2.0 (see [LICENSE](LICENSE)), as for Foundation0's other repositories.
