# Owens transcription status

The BYU PDF route returned HTTP 403 on 2026-10-28: https://scholarsarchive.byu.edu/cgi/viewcontent.cgi?article=5328&context=etd. No thesis pages or congruences were recovered, and no record system is invented here.

The comparison tool reads the repository's canonical format, requires provenance headers, rejects duplicate moduli and compares all congruences independently of order. Page markers and each input hash are retained. A header naming a transcriber is provenance, not proof of independence.

Run `python3 tools/compare_transcriptions.py first.txt second.txt` on two separately made transcriptions. Agreement does not establish coverage. Acceptance still needs the actual thesis, complete page-referenced lists, a second independent transcription and the dual coverage replay.
