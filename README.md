# cobig_misc_scripts

Repository for scripts developed and used by CoBiG² members. BEWARE! HERE BE ANTHROPOMORPHIC DRAGONS!

## TSbin 

This script converts CSV files with time series given by the [autodetec](https://github.com/maRce10/warbleR/blob/master/R/autodetec.R) script into binary sequences. An example CSV file can be found in examples/.

## FDR.py

Small script to perform several multiple test corrections. Contains a single function that takes two arguments: a list of *p*-values and the test type, which can be "FDR" (default), "Bonferroni" or "Bonferroni-Holm". Returns a list with the corrected *p*-values.

## License

Everything is under the GPLv3.
