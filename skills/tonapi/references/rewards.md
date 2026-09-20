# Rewards

5 methods from `tonapi.rewards`:

## get_validators

Get current validators with stakes, rewards, pool addresses, and nominator breakdowns.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| seqno | int \| None | no | None | Masterchain block seqno (latest by default), exclusive with `unixtime` |
| unixtime | int \| None | no | None | Unix timestamp to anchor the masterchain block, exclusive with `seqno` |
| shallow | bool | no | False | Return only basic validator info (significantly faster) |

Returns: `ValidatorsResponse`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py rewards get_validators --shallow true
```

```python
result = await tonapi.rewards.get_validators(shallow=True)
```

## get_validation_rounds

Get past and current validation rounds with boundaries, stakes, and bonuses.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| election_id | int \| None | no | None | Return the single round with this election ID |
| block | int \| None | no | None | Masterchain block seqno inside the round |
| unixtime | int \| None | no | None | Unix timestamp to anchor the masterchain block |

Returns: `ValidationRoundsResponse`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py rewards get_validation_rounds
```

```python
result = await tonapi.rewards.get_validation_rounds()
```

## get_round_rewards

Get per-validator and per-nominator reward distribution for a finished validation round.

| Param | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| election_id | int \| None | no | None | Election ID; exactly one of election_id/block/unixtime is required |
| block | int \| None | no | None | Masterchain block seqno within the finished round |
| unixtime | int \| None | no | None | Unix timestamp to anchor the masterchain block |
| shallow | bool | no | False | Return only basic validator info (significantly faster) |

Returns: `RoundRewardsResponse`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py rewards get_round_rewards --election-id 1700000000 --shallow true
```

```python
result = await tonapi.rewards.get_round_rewards(election_id=1700000000, shallow=True)
```

## get_stats

Get APY and total stake time series from past validation rounds (`apy` is a fraction here, `get_apy` returns percent).

Returns: `RewardsStats`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py rewards get_stats
```

```python
result = await tonapi.rewards.get_stats()
```

## get_apy

Get current TON blockchain APY as a percent, based on the latest completed validation round.

Returns: `float`

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/run.py rewards get_apy
```

```python
result = await tonapi.rewards.get_apy()
```
