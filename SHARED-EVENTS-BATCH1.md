# 第1批：共享事件

Date: 2026-11-15. Continues on `codex/gameplay-descriptions`, retaining all main-text batches and campaign samples.

## Scope

Translated 13 complete event families: acid rain, alchemist potions, ancient temple, animated-armour upgrade, archery tournament, bear attack, Beastmaster/Bard interaction, drinking contest, Blademaster/Orc argument, blood moon, crossroads, knights' tournament and sunset.

- `translation/shared-conversations-1.properties`: 61 content keys, covering 16 conversation branch groups (29 speaker labels, 29 dialogue/narration entries and three choice prompts).
- `translation/shared-events-1.properties`: 16 content keys, covering seven choices with their descriptions and the acid-rain battle's two-entry introduction.
- Total: 77/3,163 shared content keys (2.4%). These are key counts, not unique sentences. Remaining shared fallbacks: 3,086 (2,128 shared-level keys and 958 conversation keys).
- New runtime resources: `shared-zh.properties` (18 entries) and `shared-conversations-zh.properties` (63 entries), including two metadata entries each. Overall runtime: 4,316 entries. Main coverage remains 4,215/4,215 content keys.

## Resource loading and context

Read the supplied modding guide's localization section (pages 56–58). Scanned the installed base and DLC archives: both English shared resources occur in `aof-data.zip`, with no same-named copy in the other scanned game archives. Source bytes were compared to the extracted references.

Checked installed `I18nMessagesFactory` bytecode. `CAMPAIGN=shared` prefixes level keys with `shared.`; standalone conversations use their global identifiers with a nonempty `CONVERSATIONS` marker. Each resource must have exactly one of LANGUAGE/CAMPAIGN/CONVERSATIONS. Missing localized values fall back to English under normal engine settings. New resources contain only translated entries plus metadata, and no XML/gameplay definitions are overridden.

The editable coverage manifest declares selected event families, referenced choice prefixes and the acid-rain follow-up level. The XML checker independently follows `trigger-ref`, `play-conversation` and `goto` references for translated choices, preventing a Chinese prompt from leaving its choices or immediate outcomes untranslated.

Reviewed gameplay context: drinking-contest entry costs 100 gold; a win awards 200 gold, so the reward is not described as a 200-gold net profit. The ancient temple advances one Knight to Paladin. Acid rain has a third option using 高效解毒剂. The knights' tournament's English narration claims all knights are wounded, but the script wounds up to three and grants experience to all; the Chinese says knights were wounded without asserting every knight was hurt. Bard/Beastmaster dialogue preserves the bottle/cork joke and warning about broken strings, with provisional names 达里乌斯 and 泰娅.

## Validation and installation

The build validates source keys, duplicate keys, `${gold}` and numeric placeholders, HTML, `=BR=` markers, complete selected coverage and effective runtime key collisions before writing generated resources. Regression checks reject lost variables, repeated-placeholder loss, missing engine breaks, malformed HTML, invalid resource metadata and cross-file conversation collisions; identical level keys in different campaign namespaces remain valid.

All checks passed. The XML checker verified 16 standalone conversation groups, seven linked choices and their immediate outcomes, and matched the English reference bytes to the installed archive. Java decoded 4,316 runtime entries and verified translated text plus 3,086 remaining shared English entries in all four font styles. Main messages remain byte-identical to the installed batch 8 version. Campaign samples match HEAD and installed text; their existing CRLF/LF difference was accounted for, and they were not redeployed.

Workshop description is 5,063 UTF-8 bytes with balanced BBCode and all 32 bilingual campaign names unchanged. Backed up config and an inventory of original hashes at `backups/workshop-3840511924-before-shared-batch1-54240407`. The manifest records that the two new shared resource files did not previously exist. Installed those two files and config, verified all three against staging by SHA-256, and verified every other installed mod file is unchanged. No Git commit, GitHub push or Steam upload was performed. The pre-existing untracked `items.xlsx` was left untouched.

Real in-game review of these events remains pending, as does the separate `UXX_Please_review_us` warning. No campaign story translation is included in this batch.

Next: more complete travel-event families with choices and outcomes, then shared locations and longer side stories before the Undead campaign.
