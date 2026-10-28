# Construction methods for minimum moduli 40 and 42

This is a source-extraction record for review, not a completed reconstruction of either method or a quantitative feasibility estimate for 43.

## Sources inspected

Dalton and Trifonov, *Extreme Covering Systems*, arXiv:1905.07386v2, section 1, states that Nielsen introduced recursion for the 40 construction and Owens refined that approach for 42. This is a later source's description, not a substitute for the original algorithms: https://arxiv.org/html/1905.07386v2#S1.

Filaseta and Kalogirou, arXiv:2407.15280v1, section 1, cites Nielsen and Owens for systems reaching 42. Its principal theorem concerns a lower bound on reciprocal-modulus sums; it does not provide a reproduced 42 construction here: https://arxiv.org/html/2407.15280v1#S1.

## Extraction still blocked

The Owens PDF endpoint returned 403 on 2026-10-28: https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=5328&context=etd. The Nielsen DOI route was inaccessible through the retrieval tool: https://doi.org/10.1016/j.jnt.2008.09.016. Neither source was read in full, so their moduli, lcm, recurrences and page references remain unfilled.

For each original source, extract the congruence-generation rule, allowed prime powers, branching/pruning rule, distinctness invariant, residue-selection method, exact lcm and reported search resources. Every extracted fact needs a page or theorem reference and an independent reader check.

## Feasibility of 43

No numerical lcm estimate or runtime extrapolation is justified from the available evidence. Once the constructions are transcribed, compute exact prime-power lcm factors and benchmark both independent checkers under fixed memory/node caps. Record the fraction of unresolved branches and a resource growth curve rather than assuming bitmap enumeration is feasible.

A first search should reproduce a smaller published system before changing the minimum to 43. Distinct moduli and complete coverage remain exact acceptance conditions; a failed bounded search is not a nonexistence theorem.
