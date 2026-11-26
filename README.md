[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/iqbalbeladaz/fortune-cookie-for-the-liquidated/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/iqbalbeladaz/fortune-cookie-for-the-liquidated/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

# Fortune Cookie for the Liquidated Trader

Entry for the make.fun bounty
[Fortune Cookie for the Liquidated Trader](https://make.fun/bounty/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
($2): one fortune cookie line, at most 20 words, for a crypto trader who
has just been liquidated — judged head to head by an AI judge playing the
freshly liquidated trader, who keeps the fortune that makes them laugh
instead of cry.

## The entry

> A great fortune awaits you: it is locked in the wallet the exchange just sold.

15 words, 78 characters (gate: 1–160 characters, at most 20 words, one line).

## Why this line should win

- **Fortune voice and trading loss, both in it:** it opens with the
  classic fortune-cookie promise, "A great fortune awaits you", and the
  loss is unmistakable — the wallet, the exchange, the sale. A liquidated
  trader reads it and knows exactly whose wallet that is.
- **Laugh, not cry:** the joke is rueful and warm, never cruel or smug.
  The cookie is not mocking the trader; it is delivering the bad news in
  the most oracular way possible. The fortune is real — it just already
  belongs to someone else. The trader laughs with the cookie, not at a
  lecture.
- **One breath:** 15 words, read whole in a single breath, the way a real
  fortune does.
- **Fresh:** the double meaning of "fortune" is the turn. A fortune cookie
  promises a fortune; this one keeps the promise literally — a great
  fortune does await you — and then the punchline breaks it: the fortune
  is money, and it is locked in a wallet the exchange just sold. The last
  word, "sold", is the surprise. No stock liquidation pun, no "rekt", no
  "margin call", no "buy the dip".
- **Fortune voice throughout:** small, oracular, slightly formal phrasing
  that the punchline then breaks.

## Alternatives considered

Six lines were drafted and counted before this one was picked:

- "A great fortune awaits you: it is currently locked in a wallet you no
  longer own." (81 chars, 16 words) — same double meaning, warmer, but
  the loss is vaguer: no exchange, no sale, so a judge could read it as
  any lost wallet rather than a liquidation.
- "Your lucky numbers are 0, 0, 0, and 0 — the market has already played
  them all for you." (87 chars, 19 words) — a vivid zeroed-balance image
  and a real fortune-cookie opening, but the joke is essentially "your
  balance is zero", the obvious liquidation pun the judge is told to
  discount.
- "Fortune favors the bold — and liquidates them, usually before
  breakfast." (72 chars, 11 words) — a sharp subversion of a famous
  fortune line, but "them" puts the trader at arm's length and reads a
  touch smug; the chosen line keeps the trader as "you".
- "Your future is bright: the exchange has already sold it, at a very
  fair price." (78 chars, 15 words) — wry and trading-specific, but the
  punchline lands mid-line and the tail ("at a very fair price") is a
  second, weaker joke.
- "You will soon receive unexpected money: a refund of the fees on your
  liquidation." (81 chars, 14 words) — funny and absurd, but the
  consolation is the joke rather than a fortune, and "liquidation" stated
  outright is less of a turn than a fortune that turns out to be your own
  sold wallet.

The chosen line won because it stacks all five judge criteria in one
breath: the classic fortune opening first, the double meaning of
"fortune" as the turn, the exchange and the sale naming the loss, and
"sold" as the surprising last word.

## How it works

`main.py` writes the line to `/output/entry.txt`. It is fully
deterministic: the same bytes on every run, no input, no randomness, no
network. Standard library only.

## Verification

Before submitting, the entry was run twice locally with
`MAKEFUN_OUTPUT_DIR` pointed at two separate directories. Both runs
produced byte-identical output: sha256
`d2a8c096a963dd0f92eb4bece43e7f61780bae340f2449e4df581f1fd356315d`,
78 bytes, 15 words — inside the gate of 1–160 characters and at most 20
words. The program itself asserts both bounds before writing, so a
future edit that broke the gate would fail loudly instead of submitting
an invalid entry.

## License

MIT — see [LICENSE](LICENSE).
