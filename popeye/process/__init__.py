
"""
Basic transition system as computation model
2 dimensions :
  - compute (CPU time) -> transitions are function calls
  - storage (Memory space) -> transitions are maps

These are somewhat equivalent in theory, although not in application.

if the function calls are pure mathematical functions, memoizing (caching) is a way to trade one for the other.
It has however various limitations.
"""