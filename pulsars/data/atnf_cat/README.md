Catalogs from the ATNF Pulsar Catalog

http://www.atnf.csiro.au/research/pulsar/psrcat/

Both theirs and ones generated with their software

LIST
----

* psrcta_v1.56.db
* DM_cat_v1.56.dat 
  * Table of pulsars with DM>0 and P0>0.0001
  * ./psrcat -db_file psrcat.db -c "psrj raj decj p0 dm" -l "DM > 0.00001 " -l "p0 > 0.00001" > DM_cat.dat 
