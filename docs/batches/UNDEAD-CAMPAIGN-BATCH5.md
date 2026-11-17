# 亡灵战役第5批：王国巡逻队

2026-11-16。本批覆盖巡逻队事件、战斗对话、胜利叙事与直接相连的失败路线开场，以返回世界地图为边界。内部记录包含剧情；公开Workshop简介仅更新覆盖数字。

## 范围与进度

- 新增45条内容键：Level15共2条，Level16共11条，Level17共1条，LevelSecret01b共1条；U05_Bowman_death共12条，U05_Knight_raise共10条，U05_Monk_death共4条，UXX_Vision_1a共2条，UXX_Krill_wight共2条。各声明组均完整覆盖。
- `undeadcampaign`：109/344；`undeadcampaign-conversations`：142/388；合计251/732（34.3%），另有4条元数据。三篇长叙事各只占一个文本键，条目数不是字数或全游戏完成度。
- 沿用克里尔、诺娅、加雷思爵士、骑士、僧侣、尸妖与灵魂之铃；地点采用王国巡逻队 (Kingdom Patrol)、暗影沼泽 (Shadowmarshes)、雾磨镇 (Mistmill)、兽人丘陵 (Orcs' Hills)。不将泛指“人世”或普通废墟擅自改成具名地图地点。
- 保留诺娅以尸体阻挡敌人的笑话及脚踝礼俗的反讽，克里尔的台词延续轻蔑、残酷的口吻。未补写原文没有的人物关系或结局。

## 流程与依赖核对

- 对照本地亡灵归档的战役XML、五份新增对话XML及英文properties。Level15退出时锁定地图节点、给予500金币并进入Level15b；商店随后转入Level16。Level15b无独立英文文本键、无对话调用，兵种和物品名称来自正文，不计为新增已译组。
- 解压U05_Kingdom_Patrol.brd的zlib载荷，按序列化字符串长度核对U05_Bowman_death、U05_Knight_raise及U05_Monk_death引用。保留原脚本的ignore-focus等行为，不把后续序列化字节误认作对话名。
- Level16初始化的UXX_PlayerUnit_death、UXX_Krill_impatient、UXX_PlagueZombie_detonate、UXX_Krill_damage及UXX_Noea_damage均已译，本批直接复用。灵魂之铃奖励条件是敌方Soldiers种族数量为0且回合数LESS_EQUAL_12，译为“在第十二回合结束前消灭所有士兵”，不扩大为消灭所有敌人。
- 胜利后给予全队75经验；若持有骨龙／幽灵龙且第三级亡灵据点未解锁，则播放已译UXX_BoneDragon_remove并移除对应单位，再进入Level17。Level17解锁Level19、Level22与Level24；仅在show-visions-enabled为yes时播放UXX_Vision_1a，随后返回世界地图。幻象第0项只有图片，文本保留第1项索引，不编造第0项对白。
- 失败后按同样的龙类／据点条件移除对应龙类，但没有离队对白，随后进入LevelSecret01b。其叙事及UXX_Krill_wight提示本批完整译入；原脚本将英雄转为尸妖、切换肖像、补充单位和经验并解锁成就，最后解锁Level30与Level33并返回世界地图。此处不新增选择按钮；“是否继续”只是原有提示。
- LevelSecret01b还执行ask-for-review。它是引擎命令，不是本批五组对话中的文本键；先前UXX_Please_review_us警告仍未确诊，不宣称本批解决它，也不改动脚本以隐藏警告。
- 五份新增对话XML没有额外commands分支。检查本批关卡命令中的全部显式UXX对话引用，均已包含在战役覆盖声明中。后续Level19/22/24及Level30/33不因解锁而计作已译；据点升级对白仍是另行待办。

## 构建与验证

- `build_translation.py`通过完整声明组、源键、重复键、占位符及次数、HTML、=BR=、元数据、命名空间和ASCII Java properties检查。新增45条的HTML标签顺序及属性逐一与英文一致。
- Java `inspection/CheckPilot.java`通过：6,678条运行时条目、1,446条英文回退，Noto Sans SC的常规／粗体／斜体／粗斜体以及引擎NBSP和项目符号均通过覆盖检查。
- 与批次开始快照逐键比较：所有既有译文值保持不变；正文与通用译文及对应运行时properties未改变。通用覆盖保持2,198/3,163，通用报告只更新全项目运行时条目总数。
- 更新战役声明、覆盖报告、进度、术语和文档索引；公开简介只把206/732（28.1%）改成251/732（34.3%），保留双语战役名、预览和无剧透格式，低于7,999 UTF-8字节上限。
- `git diff --check`通过。未安装、提交、推送或上传本批；当前安装版仍为战役第4批。游戏内检查继续暂缓，自动检查不证明排版或所有分支在游戏中正确。

## 下一批

优先继续Level19及其后续商店／战斗链，核对对应U06对话与新出现的UXX依赖。Level22、Level24以及失败路线后续Level30、Level33仍待推进；据点升级对白另行跟踪。复用已经完成的战斗反应，不改动通用资源负责人的译文。
