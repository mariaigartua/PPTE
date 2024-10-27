# Usage Information

(C) Copyright 2020, all rights reserved. This dataset was developed by Carnegie
Mellon University under the
[Usable Privacy Policy Project](www.usableprivacy.org). For any questions about
this data, including licensing, please contact Prof. Norman Sadeh
(sadeh@cs.cmu.edu).

The annotations are made available for research, teaching, and scholarship
purposes only, with further parameters in the spirit of a Creative Commons
Attribution-NonCommercial License.

If you use this dataset as part of a publication, you must cite the following
paper:

Finding a Choice in a Haystack: Automatic Extraction of Opt-Out Statements from
Privacy Policy Text. Vinayshekhar Bannihatti Kumar, Roger Iyengar, Namita Nisal,
Yuanyuan Feng, Hana Habib, Peter Story, Sushain Cherivirala, Margaret Hagan,
Lorrie Cranor, Shomir Wilson, Florian Schaub, and Norman Sadeh. In Proceedings
of The Web Conference, Taipei, Taiwan, April 2020.

Additionally, please email Norman Sadeh (sadeh@cs.cmu.edu) with copies of
publications, technical reports, and other papers that use this data.
We may feature your work on the Usable Privacy Policy Project website.

## Binary Data

Hyperlinks were labeled to indicate whether or not they were opt-out links. See
the file `binary_example.py` for details about how to access these labels. This
script requries [SQLAlchemy](https://www.sqlalchemy.org). We tested it with
version 1.3.16 of SQLAlchemy. You can see all available fields defined in our
database schema in the file `binary_data/models.py`. If you prefer not to use
Python and SQLAlchemy, you can explore the database by opening the file
`binary_data/policies.db` with
[DB Browser for SQLite](https://sqlitebrowser.org).

## Category Data

Opt-Out hyperlinks were labeled to indicate the category of data involved. See
the file `category_example.py` for details about these labels.

### Credits

This research was mainly conducted as part of the NSF SaTC Frontier project on
Usable Privacy Policies (CNS-133059) with additional funding provided
by NSF grants CNS-1801316 and CNS1914486, and a DARPA Brandeis grant on
Personalized Privacy Assistants (FA8750- 15-2-0277). Further support was
provided under a National Science Foundation’s Graduate Research Fellowship
Program under Grant Nos. DGE1252522 and DGE1745016.
