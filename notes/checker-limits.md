# Exact coverage checks

A periodic congruence system covers the integers exactly when it covers one complete least-common-multiple period. The first checker builds that bitmap.

The second checker starts with all integers and recursively partitions a residue class r modulo M into classes modulo lcm(M,m). It discards a class only when an input congruence covers every member. Incompatible congruences are removed using the gcd criterion. An empty compatible set produces an uncovered witness class. The implementations share no code.

Both algorithms are bounded. A resource error is unresolved, never a negative mathematical verdict. The complete source header, transcription page references and input hashes remain necessary for the historical systems.
