# COP4533 Programming Assignment 2
Ryan Goodman (UFID: 46759399)
## Instructions to Run
- Navigate to /src and run the following commands. Note that you should use whatever python alias your device has.
> "python inputPreparation.py k m" where $k$ and $m$ correspond to the cache size and number of requests, respectively
> "python policies.py"
## Other Info
- The input.txt file format should match the format given on the assignment exactly; there is no guarantee that things will work if a different format is used (inputPreparation.py will follow this input format).
- The assignment did not specify how to handle a tiebreaker with OPTFF, so I chose to use FIFO. I chose to generate the requests by randomly generating $m$ integers from $1$ to $m$ since this was not specified either.
- The responses to the written component are in the file "PA2.pdf".
