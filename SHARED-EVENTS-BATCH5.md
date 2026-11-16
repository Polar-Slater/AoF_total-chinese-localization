# 第5批：共享事件

Date: 2026-11-15. Continues on `codex/gameplay-descriptions`. In-game testing remains deferred; natural Chinese and bilingual place names remain user requirements.

## Scope and milestone

Translated the remaining 40 `SGE_` event families plus `SXX_Gambler`: city guards, Dwarven merchants/gangs/tavern, recruitment and unit construction, village fires, graveyards, three witches, furniture warehouse, royal gifts, gambling and other travel encounters. Exact families and linked choices are declared in `translation/shared-coverage.json`.

- `translation/shared-conversations-5.properties`: 76 content keys in 55 conversation groups (71 keys in 52 SGE groups plus five gambler keys in three groups).
- `translation/shared-events-5.properties`: 188 keys: 172 fields for 87 choices, plus 16 dialogue entries in three follow-up battles. Two city-guard options have no source description field; no description was invented.
- Added 264 keys. Cumulative shared coverage: 902/3,163 (28.5%), comprising 492 standalone conversation keys and 410 level/choice keys. Counts include repeated speaker labels.
- All 487 `SGE_` conversation keys and all 410 `LevelGlobalEvent*` keys are now covered. The build enforces this milestone. This is not completion of all shared text: 2,261 keys remain (1,734 shared-level and 527 other conversation keys).
- Cumulative scope: 118 event families, 191 standalone conversation groups, 194 choices and eight direct follow-up levels. Seven levels have translated dialogue; the Three Witches battle has no extracted text. Total runtime: 5,141 entries.

## Translation and mechanics

Preserved unit terminology, recruitment and ritual costs, sacrifice counts, `${gold}`, `${shared-gambler-debt}`, `${selected-unit-name}` and `${selected-unit-original-name}`. The gambler's Oracle option uses 神谕者. The Blood Sisters are 鲜血姐妹; their sacrifice opens a unit selector, and cancelling returns to the event rather than killing a unit.

Place/store names retain English: 伊凯乌斯家具 (IKEUS FURNITURE), with the sign's original capitals, and 风车磨坊 (Windmill), matching the shared map label. Previously approved 三魔峰 (Three Devils) and 冰原 (Iceland) remain unchanged. Generic unnamed forests, villages and caves remain ordinary Chinese nouns.

Checked option commands and follow-up battle XML. Source Drunken Dwarf tooltip claims 50% theft success, but the script uses three modulo branches: two item rewards and one battle. The Chinese describes a chance to steal and the risk of fighting without repeating an unreliable numeric probability. No gameplay command was changed. Repeated refusal to pay Dwarves' tavern bills increases departure risk; the Chinese preserves that condition. Royal gifts track repeated gifts before a return gift, so the translation does not promise an immediate reward for every payment.

The Three Witches and Dwarf Merchant trade choices lead to a generic random shop, outside this batch's resource scope. The Windmill event can unlock its rebuilding location; that separate location narrative remains for the next shared-location phase. Completing global-event text does not imply those linked generic shops/locations are translated.

## Validation and installation

Passed exact 264-key checks, preservation of every previous runtime value, build coverage, HTML, placeholders, `=BR=` markers and runtime namespaces. XML validation covers 191 groups, 194 choices, three callback/trigger targets and eight direct follow-up levels. Added explicit textless-level declarations checked against both source properties and actual XML; callback traversal now follows `exec-trigger` as well as manual unit selection, with cycle protection.

Java decoded 5,141 entries and checked translated text, engine symbols and 2,261 remaining English fallback entries in four font styles. The final Windmill suffix adds only already-covered Latin letters; rebuilt and verified staging/installed bytes after that wording update. Main messages and campaign samples remain byte-identical to the pre-batch snapshot.

Workshop description includes `#5 共享事件`, 5,776 UTF-8 bytes, balanced BBCode, and all 32 bilingual campaign/expansion names preserved. Backup: `backups/workshop-3840511924-before-shared-batch5-e8f18176`; an additional pre-suffix snapshot is in `backups/before-windmill-place-label`. Installed only both shared resources and config. Final SHA-256 hashes match staging; all other installed mod files are unchanged.

No game test, Git commit/push or Steam upload was performed. `items.xlsx` remains untouched. Next: shared locations and longer side stories, then the Undead campaign; deferred game review does not block translation.
