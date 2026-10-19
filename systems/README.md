# Covering systems

One plain-text file per covering system, named after its author and its smallest modulus, such as `owens-42.txt`.
Both coverage checkers read these files, and both must agree on every one.

## Format

- **Congruences.** One per line, written `a mod m`. The modulus `m` is a whole number of at least 2, and the
  remainder `a` is a whole number from 0 to m − 1. So `1 mod 4` means "n leaves remainder 1 when divided by 4".
  No modulus appears twice.
- **Comments.** A line that starts with `#` is a comment. Use comments inside the list to give page references, such
  as `# page 31`.
- **Header.** The comments at the top of the file, one `# key: value` per line:
  - `source`: the publication the system comes from, with authors, title and year
  - `link`: where to find it
  - `pages`: the pages the congruences were copied from
  - `transcribed by`: who made this file, and the date
  - `minimum modulus`: the smallest modulus the source claims
- If the source writes a remainder outside 0 to m − 1, reduce it and say so in the header.
- Blank lines are ignored.

A checker confirms three things: no modulus appears twice, the smallest modulus equals the header's
`minimum modulus`, and every integer satisfies at least one congruence.

## Example

The small system from the README. It is not from a publication, so `link`, `pages` and `transcribed by` are left out.

```
# source: example covering system for testing the checkers
# minimum modulus: 2
0 mod 2
0 mod 3
1 mod 4
5 mod 6
7 mod 12
```
