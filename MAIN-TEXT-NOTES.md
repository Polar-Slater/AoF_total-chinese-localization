# Main text: batch 1 (unreleased)

This batch covers shared interface and gameplay text in `messages-en.properties`; existing campaign samples are retained. The user subsequently restored the wider order: terminology, gameplay descriptions, shared events, then campaigns starting with the Undead campaign. Current work is terminology review; see `LOCALIZATION-PLAN.md` and `TERMINOLOGY.md`.

## Scope

| Editable batch | Entries | Contents |
| --- | ---: | --- |
| `translation/gameplay-basics.properties` | 129 | Stat labels/tooltips, inventory prices and actions, item categories/rarities, common skills and statuses |
| `translation/bestiary-basics.properties` | 54 | Names and descriptions for 27 Human, Undead and Goblin units |
| `translation/combat-log-basics.properties` | 137 | Hits, kills, injuries, morale, common status effects, healing, lifedrain and soul capture |
| Total added | 320 | No overlap with earlier batch keys |

The 27 units include the Footman, Royal Guard, Necromancer and Skeleton Warrior shown in the user's screenshots, plus basic human troops/casters, skeleton variants, zombies, other common undead, three Goblin types and two alchemy specialists. This is not a complete bestiary translation.

The current main source contains 4,221 keys. The built main file supplies 809 keys, including locale/font metadata, leaving 3,412 to English fallback. The original 481-entry Phase 1 count is kept separate. All runtime files together contain 823 entries, including the 14 unchanged campaign sample entries/metadata. Entry counts are not word counts or an estimate of overall translation completion.

## Terminology

`TERMINOLOGY.md` consolidates the working baseline. Retain the initial glossary in `PHASE1-NOTES.md`, with these batch additions:

| English | Chinese |
| --- | --- |
| Attack / Defence / Speed | 攻击 / 防御 / 速度 |
| Ranged Attack | 远程攻击 (compact stat label: 远攻) |
| Footman / Royal Guard | 步兵 / 皇家卫士 |
| Necromancer / Skeleton Warrior | 死灵法师 / 骷髅战士 |
| Goblin | 地精 |
| Wight / Lich / Banshee | 尸妖 / 巫妖 / 报丧女妖 |
| Alchemist / Artificer | 炼金术士 / 炼金工匠 |
| Defensive Stance | 防御姿态 |
| Blocked / unblockable | 受牵制 / 不受牵制限制 |
| Backstab / Greater Backstab | 背刺 / 强效背刺 |
| Lifedrain / Soul Capture | 生命汲取 / 灵魂捕获 |
| Raise Dead / Resurrection | 唤起亡者 / 复活术 |
| Ensnared / Entangled | 网缚 / 缠绕 |
| Poisoned / Corrosion / Disease | 中毒 / 腐蚀 / 疾病 |
| High Morale / Panic | 高昂士气 / 恐慌 |
| Avatar / Illusion | 化身 / 幻象 |
| Hide in Shadow / Invisibility / Shadow Oil | 潜入暗影 / 隐形术 / 暗影油 |
| Relic / Artefact / Treasure | 圣物 / 宝物 / 财宝 |

`unblockable` means an action remains usable while an adjacent enemy prevents most spells and ranged attacks (`S_HAS_BEEN_BLOCKED_HINT`). It does not mean the attack ignores defence or cannot be parried.

Combat keys containing `OVERLOADED` display generic "affected" in the English source. Their translations preserve that displayed meaning rather than inventing an overload mechanic. Existing source misspellings such as `ENTAGLED` remain unchanged in identifiers.

Short stat abbreviations now use two-character Chinese labels. The hit-chance tooltip expresses each point of Attack/Defence difference as 10 percentage points, preserving the source's 50% starting chance. Placeholders, number values, item rarity markers and functional HTML are retained.

## Build and review

Run `build_translation.py`, then `prepare_workshop.py` with the existing item's path and owner ID. Validate the staged package with the game's Java runtime and `inspection/CheckPilot.java` as described in README.md. Keep the source resources and local test font out of Git.

In-game checks still required for this batch:

1. Open the bestiary and inspect Footman, Royal Guard, Necromancer and Skeleton Warrior names/descriptions, including the narrow stat column.
2. Hover over stats and Defensive Stance; check Chinese wrapping and the explanation of enemy adjacency.
3. Inspect inventory prices, item categories, identification and equipment dialogs without needing to buy or sell anything.
4. Review an ordinary battle's hit/kill, morale, lifedrain and soul-capture messages with substituted unit names and numbers.

The previously reported `UXX_Please_review_us` conversation validation warning has not been diagnosed by this batch. Passing text and font checks does not establish that all dialogs fit in game.

Subsequent screenshot review confirmed missing tooltip-prefix glyphs in SimHei. Batch 2 replaces it with static regular Noto Sans SC and expands validation to engine symbols and English fallback; actual game confirmation is pending. See `MAIN-TEXT-BATCH2.md` for current totals and testing; the counts above describe batch 1.
