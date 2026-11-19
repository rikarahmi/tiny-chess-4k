# tiny-chess-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/rikarahmi/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/rikarahmi/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

**Tiny Chess 4K** — a complete chess engine in 4 KB of Python: 0x88 board, alpha-beta with quiescence (captures, promotions, check evasions), transposition table, null-move pruning, late-move reductions, and incremental evaluation. It plays the make.fun gauntlet over the environment HTTP API — reads the prompt file, polls `/game`, and posts UCI moves to `/move` until every game ends. The source is LZMA-compressed and self-extracting on import; the engine is original work, written from scratch.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18100 MAKEFUN_PROMPT_FILE=/input/prompt.txt python3 -P -s main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
