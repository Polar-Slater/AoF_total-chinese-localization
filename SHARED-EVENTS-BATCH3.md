# 第3批：共享事件

Date: 2026-11-15. Continues on `codex/gameplay-descriptions`. The user explicitly deferred in-game testing to prioritize translation. Automated text/resource checks continue; no game session was launched.

## Scope

Translated 20 event families: Dryad, DwarfBeggar, ForestElf, GoblinTreasure, Insectoids, MageTrickster, ManaShard, Monk, OldMonastery, OutpostRuins, PrimeSource, RadiatingTunnel, SnakeStaff, StolenGold, SuccubusLost, TargetPractice, UndeadAltar, Unicorn, WargsHowl and WillOWisp.

- `translation/shared-conversations-3.properties`: 142 content keys across 43 conversation groups.
- `translation/shared-events-3.properties`: 84 content keys, covering 40 choices with their descriptions and four entries for two follow-up battle introductions.
- Added 226 content keys. Cumulative shared coverage: 482/3,163 (15.2%), comprising 294 standalone conversation keys and 188 level/choice keys. These counts include repeated speaker labels, not only unique sentences.
- Cumulative selected scope: 46 event families, 96 standalone conversation groups, 91 choices and three follow-up levels. All runtime resources total 4,721 entries. Remaining shared fallback: 2,681 keys (1,956 level/choice, 725 standalone conversation).

## Translation and context

Preserved the Dwarf Beggar's shabby sales patter, the Dryad's friendly conversation with a bear, and the Zombies' broken speech. Prime Source is provisionally 原初之源, distinct from the skill Magic Source／魔力源泉; Bartolome is provisionally 巴托洛梅. Gnomish uses 侏儒, not 矮人. Reused 林妖、座狼、鬼火、魔力碎片、变异矮人、烈焰弓箭手 and 永久创伤 from existing terminology.

Checked the actual shared-event XML, including initial triggers and option commands. The Forest Elf branch upgrades two nonhero Bowmen to Rangers; the Chinese outcome specifies two. Stolen Gold removes 500 gold initially; the thieves' recovery branch awards 1,000 gold, not a 1,000-gold net profit. Target Practice bets are 100 or 200 gold. The Dwarf's gallery entry costs 5 gold; the 100/300-gold prices in his speech are sales dialogue, not additional choice fees.

The Goblins' argument causes two permanent wounds. The Radiating Tunnel replaces a Dwarven Warrior with a Mutated Dwarf. The monastery can cause a battle or recruit Monks. Prime Source retains both mage-death warnings; its direct battle introduction and the Warg ambush introduction are translated. The ghost-light and stolen-gold random battles also have their opening conversations included.

Retained source distinctions without inventing gameplay changes: the Dryad conversation's speaker is Dire Bear, while its generic bear reward actually creates a cavebear and unlocks direbear knowledge. The outpost narration describes Fire Archer evolution; its command gives a Fire Archer. That narration remains translated as written, with actual progression behavior left for deferred game review. No XML or gameplay logic was changed.

## Validation and local installation

Passed exact new-key coverage, placeholders, `=BR=` preservation, HTML, metadata/namespaces and XML-linked branch checks. Java decoded 4,721 runtime entries and verified translated text, engine tooltip symbols and 2,681 remaining English fallback entries in four font styles. Every previous runtime value is preserved; main messages and both campaign samples are byte-identical to the pre-batch snapshot.

Updated the Workshop description with `#3 共享事件`, cumulative progress and deferred game-review status. Balanced BBCode, 5,423 UTF-8 bytes, all 32 bilingual campaign/expansion names unchanged. The staged resources match the validated build.

Backup: `backups/workshop-3840511924-before-shared-batch3-f1b6a75a`. Installed only both shared runtime resources and config. Verified SHA-256 against staging and every other installed mod file unchanged. No Git commit/push or Steam upload. The unrelated untracked `items.xlsx` remains untouched.

In-game testing is deferred at the user's request, not a prerequisite for the next translation batch. Main batches 6–8 and shared batches 1–3 remain unreviewed in game; the separate `UXX_Please_review_us` warning remains unresolved. Continue remaining complete shared travel events, then shared locations and longer side stories, followed by the Undead campaign.
