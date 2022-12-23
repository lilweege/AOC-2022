from dataclasses import dataclass
from functools import cache
from math import prod
from re import findall

FILE = "input/19.txt"
# FILE = "sample.txt"
f = open(FILE, "r")


@dataclass
class Blueprint:
    num: int
    ore_ore_cost: int
    clay_ore_cost: int
    obs_ore_cost: int
    obs_clay_cost: int
    geo_ore_cost: int
    geo_obs_cost: int

blueprints = [Blueprint(*map(int, findall(r'(-?[\d]+)', line))) for line in f.readlines()]


def num_geo(bp, num_mins):
    # FIXME: This is slow...
    # There is probably a lot of pruning I missed
    @cache
    def dfs(mins,
            ore_amt, clay_amt, obs_amt, geo_amt,
            ore_bot, clay_bot, obs_bot, geo_bot):

        if mins == 0: return geo_amt

        ans = 0
        new_ore_amt = ore_amt + ore_bot
        new_clay_amt = clay_amt + clay_bot
        new_obs_amt = obs_amt + obs_bot
        new_geo_amt = geo_amt + geo_bot

        # Build geode bot
        if ore_amt >= bp.geo_ore_cost and obs_amt >= bp.geo_obs_cost:
            ans = max(ans, dfs(mins-1,
                new_ore_amt-bp.geo_ore_cost, new_clay_amt, new_obs_amt-bp.geo_obs_cost, new_geo_amt,
                ore_bot, clay_bot, obs_bot, geo_bot+1))

        else:

            # Build obsidian bot
            if obs_bot < bp.geo_obs_cost and ore_amt >= bp.obs_ore_cost and clay_amt >= bp.obs_clay_cost:
                ans = max(ans, dfs(mins-1,
                    new_ore_amt-bp.obs_ore_cost, new_clay_amt-bp.obs_clay_cost, new_obs_amt, new_geo_amt,
                    ore_bot, clay_bot, obs_bot+1, geo_bot))

            else:

                # Build clay bot
                if clay_bot < bp.obs_clay_cost and ore_amt >= bp.clay_ore_cost:
                    ans = max(ans, dfs(mins-1,
                        new_ore_amt-bp.clay_ore_cost, new_clay_amt, new_obs_amt, new_geo_amt,
                        ore_bot, clay_bot+1, obs_bot, geo_bot))

                # Build ore bot
                if ore_bot < max(bp.clay_ore_cost, bp.obs_ore_cost, bp.geo_ore_cost) and ore_amt >= bp.ore_ore_cost:
                    ans = max(ans, dfs(mins-1,
                        new_ore_amt-bp.ore_ore_cost, new_clay_amt, new_obs_amt, new_geo_amt,
                        ore_bot+1, clay_bot, obs_bot, geo_bot))

                # Build nothing
                ans = max(ans, dfs(mins-1,
                    new_ore_amt, new_clay_amt, new_obs_amt, new_geo_amt,
                    ore_bot, clay_bot, obs_bot, geo_bot))

        return ans

    init_wait = min(bp.ore_ore_cost, bp.clay_ore_cost)
    num_geo = dfs(num_mins - init_wait, init_wait, 0, 0, 0, 1, 0, 0, 0)
    return num_geo


def part1():
    print(sum(bp.num * num_geo(bp, 24) for bp in blueprints))

def part2():
    print(prod(num_geo(bp, 32) for bp in blueprints[:3]))


part1()
part2()
