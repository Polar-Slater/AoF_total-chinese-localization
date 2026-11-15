# Phase 1: menus, settings and battle controls

Workshop item: **3840511924**. Language: **Chinese (Simplified) - Test**.

## Delivered

481 translated entries cover the main menu, common buttons and tabs, settings labels and explanations, battle commands and keyboard/touch help, save/load confirmations, difficulty selection, multiplayer setup, and related dialogs. All 135 entries in the main buttons/tabs block and all 197 entries in the main settings block are covered. Existing pilot campaign/dialogue translations are retained.

Story text, most unit/item/skill descriptions, tutorials and detailed combat log messages remain outside this batch and fall back to English. Proper names such as Steam Deck, Java and OpenAL remain unchanged. The language selector deliberately uses an English label because the English font cannot display Chinese before the language changes.

## Test in the game

Restart the game through Steam, then select **Chinese (Simplified) - Test**.

1. Check the main menu and save/load dialogs.
2. Open every settings tab; hover over the settings to check tooltips, line wrapping and clipping.
3. In battle, check 战斗日志, 显示缩放, 撤销, 结束回合 and the F1 shortcut guide.
4. Check difficulty selection and multiplayer setup labels.
5. Run Workshop Manager validation. The earlier missing-conversation warning for `UXX_Please_review_us` is a separate unresolved issue.

## Editing and rebuilding

Edit the UTF-8 files in `translation/`: `ui-phase1.properties`, `settings-tooltips.properties`, and `menu-dialogs.properties`. Run `prepare_workshop.py` with the bundled Python runtime to validate and build `workshop-package`. This prepares local files only; it does not install or upload them. The baseline is `messages-zh.properties`; batch files override its entries. `prepare_pilot.py` preserves existing editable baseline files, but generates only the pilot runtime; run `prepare_workshop.py` afterwards to include the full current batch.

`build_translation.py` checks duplicate/unknown keys, placeholder counts, balanced HTML and coverage of the source buttons/settings sections, then emits ASCII files with Java Unicode escapes. The bundled game Java runtime also verified all 503 package entries and font coverage. These checks do not establish that every dialog fits on-screen.

Two ambiguities in the original English text were preserved pending behavioral verification: the proxy username/password labels are swapped, and the AI-during-animation label conflicts with its explanatory tooltip. Malformed HTML in the first-run/restart and smart-camera messages was repaired in translation.

## Initial terminology

| English | Chinese |
|---|---|
| Campaign | 战役 |
| Battle | 战斗 |
| Turn | 回合 |
| Unit | 单位 |
| Team | 队伍 |
| Faction | 阵营 |
| Skill | 技能 |
| Trait | 特性 |
| Morale | 士气 |
| Hit Points | 生命值 |
| Magic Points | 魔法值 |
| Items Cache | 物品仓库 |
| Crafting resources | 制作材料 |
| Evolve | 进阶 |
| Smart camera | 智能镜头 |

This remains a local development package, using the local test font. Nothing is uploaded to Steam by these scripts.
