# 1️⃣🐝🏎️🐍 One Billion Row Challenge using Python

[Link](https://github.com/gunnarmorling/1brc/tree/main) to original challenge.

Though
the [fastest submission](https://github.com/gunnarmorling/1brc/blob/main/src/main/java/dev/morling/onebrc/CalculateAverage_thomaswue.java)
runs in a whopping 1.5 seconds!!
The Python implementation is much simpler and easier. Although Python is regarded as one of the slowest
languages due to its dynamically typed nature. But the extensive package ecosystem makes up for it.

Packages like [DuckDB](https://duckdb.org/) are written in C++ and provide almost the same level of performance while
being easier to implement.

## Generate the Data

Clone the [original repository](https://github.com/gunnarmorling/1brc/tree/main) and follow the steps in the to
generate `measurements.txt`

## Solution 1:

This is the pure python solution `pure_python.py`. This takes 22 minutes to run.

## Solution 2:

This solution uses the DuckDB package to speed up the execution time to around 9.5 seconds on a
instance with 48 core
and 96 GB RAM.
