# 永生之旅独立对白第1批：14组AXX对白

2026-11-21。按用户指定范围完成独立扩展对话，保持通用第29批及亡灵战役译文不变。内部说明包含剧情，公开简介仅列资源进度。

## 范围与统计

新增 `translation/alchemistdlc-conversations-zh.properties`，共175条内容、2条元数据。原文为 `source/aof-alchemist-dlc/alchemistdlc-conversations-en.properties`，对照同一归档中的对白XML及 `campaign/level/shared/alchemistdlc.xml`。

| 完整对白组 | 内容键数 |
| --- | ---: |
| AXX_Welcome | 4 |
| AXX_Human_intro | 30 |
| AXX_Undead_intro | 34 |
| AXX_WellOfWishes_intro | 6 |
| AXX_Well_intro | 12 |
| AXX_Well_lost | 6 |
| AXX_ForgottenMine_intro | 8 |
| AXX_DragonStatue_intro | 10 |
| AXX_DragonStatue_fail | 4 |
| AXX_DragonStatue_base | 4 |
| AXX_DragonStatueSeal_whole | 10 |
| AXX_DragonStatueVsTalnes_select | 23 |
| AXX_SeaPortal_intro | 16 |
| AXX_RedCrab_exit | 8 |
| 合计 | 175 |

独立对话文件覆盖175/275（63.6%）。尚余九组战斗反应34条及七组回归提示66条；这些条目继续回退英文。14组完成不等于整个扩展完成，也不证明全部战场动态文本已覆盖。通用文件仍为3,163/3,163，亡灵战役仍为251/732。全项目运行时含元数据共7,820条。

## 文风与术语

塔尔尼斯沿用学究、自信又容易慌乱的语气，对骑士和死灵法师使用礼貌措辞。克里尔保留讥讽和不耐烦；开场的“说上一句话／不止一句”承接原文双关。骑士的奉承与加半分笑话保留，不额外增加人物关系。

沿用塔尔尼斯、克里尔、巨龙雕像、老兵及许愿井 (Well of Wishes)。普通岔路口与地下要塞不擅自命名。仪式咒语使用拟音，保持中断和惊呼的节奏；提示正文不写入脚本标识。

封印拼合提示原文称 Black Dragon Seal，实际给予 `DragonStatueSealWholeItem`。中文保留该提示的“黑龙封印”，其他资源仍区分完整封印和献祭奖励黑龙封印。此命名差异已记入 `docs/GAME-BUGS.md` TXT-005，不修改奖励脚本。

## XML与选项核对

- 14组的每个name、text及selection-text字段均与原文及XML索引对应。五个纯图片索引保留空缺：Human_intro 14、Undead_intro 16、WellOfWishes_intro 2、DragonStatue_base 0、DragonStatueSeal_whole 1；不编造对白补齐索引。
- `LevelAlchemist01` 的欢迎、人类／亡灵条件分支与离场对白，以及后续矿井、雕像、海上传送门和蟹神战后调用均已核对。14组在关卡脚本中的引用完整；对白XML本身没有额外commands。
- 仪式选择页保留原HTML标签顺序和9个 `<br>`，共10个文本行段，含原来的空行。自动检查不证明游戏内的实际文字宽度或自动折行。
- 两个 `trigger-ref` 分别指向 `LevelAlchemist16b.on-select-1/2`，按钮沿用已译通用文本。救援指向LevelAlchemist17（13条现有内容），不干预指向LevelAlchemist18（11条现有内容）。前者升级既有塔尔尼斯为炼金工匠，后者移除塔尔尼斯并给予BlackDragonSealItem；未新增单位或奖励说明。
- 仅新增独立CONVERSATIONS资源。未新增重复的 `alchemistdlc-zh.properties` 关卡文件；独立与通用关卡版本差异仍依通用第29批的来源边界处理。

## 构建与交付

新增 `translation/expansion-coverage.json`，声明独立扩展对白组；构建检查源键、完整组、占位符次数、HTML结构、元数据、引擎换行及运行时命名空间。新增 `inspection/check_expansion_dialogues.py` 对照归档验证XML字段、纯图片索引和选择结果。

Java解码7,820条运行时条目，检查四种字体样式及581条英文回退（亡灵481条、此对话文件100条）；正文和两个通用文件回退均为零。物品页布局夹具保持497/500。既有可编辑译文和五个运行时文件逐字节不变。详见 `inspection/expansion-validation.json`、`inspection/expansion-xml-validation.json` 和 `inspection/alchemist-dialogue-batch1-validation.json`。

简介沿用用户的简洁格式，只更新扩展对白分类说明及文件进度，保留所有双语战役名。未安装、提交、推送或上传本批，游戏内验证继续暂缓。下一步可按用户指令补齐九组战斗反应，再处理回归提示或其他扩展。
