# 通用事件与通用对话第20批：世界之结

## 范围与进度

- `translation/shared-conversations-20.properties`：8条，完整覆盖 `SXX_WorldKnot_enter`、`SXX_WorldKnot_VictoryReturn` 和 `SXX_WorldKnot_FailureReturn`。
- `translation/shared-events-20.properties`：26条，完整覆盖 `LevelWorldKnot01`、`LevelWorldKnot03a/03b/03c` 的现有文本键。
- 三个战前商店 `LevelWorldKnot02a/02b/02c` 没有独立文本键，加入无文本关卡检查，不虚构译文。
- 新增34条，累计 **2,287/3,163（72.3%）**：通用事件1,277/2,144（59.6%），通用对话1,010/1,019（99.1%）。剩余876条，包括867条通用事件和9条通用对话。
- 剩余对话为七条 `SXX_AdvertDialog_*` 选择提示及两条 `SXX_Debug` 文本；不把这些英文回退计为已译。
- 主消息4,215条、当前仓库亡灵战役206条不变；生成的运行时含元数据共6,722条。

## 术语与叙述

World Knot 与 World's Knot 统一译作世界之结，各处保留原文对应的英文拼写。chronomancy 译作时间魔法，timeline 译作时间线；不额外扩展故事中的时空设定。

入口物品沿用亡灵之冠、恶魔之心、染血战斧。失败对白保留挑战艰难和安然返回的含义；胜利对白保留是否改变历史的悬念，不将其改成确定发生的剧情后果。

## 三项挑战核对

依据 `aof-data.zip` 内 `com/aof/resource/campaign/level/shared/shared-worldknot.xml` 核对：

- 地点发现条件包含非教程、进度至少0.9，以及森林或矮人战役限制；本批不宣称所有战役均可进入。
- 三个入口分别检查对应物品及 `world-knot-battle-A/B/C-available`。进入即将相应状态设为 `no`，因此限制是每项挑战只能尝试一次，不是每次胜利后才锁定。
- 入口检查持有物品，但所查触发器没有移除入口物品的命令；译文用“使用”，不写成献祭或消耗。
- 各入口均先清空并保存单位缓存A，再执行 `remove-units-but-heroes * false`，播放进入提示，转到各自的战前商店。商店退出分别进入对应战斗。
- 三场战斗的胜利和失败分支均执行 `retrieve-units-cache A`、`clear-units-cache A`，播放对应返回对白，再回到 `LevelWorldKnot01`。不将失败写成战役终结。
- “任一英雄阵亡即返回”沿用原始战斗提示；本批已核对关卡层面的胜败处理，不将其写成已逐项实测战场内部判定。军队恢复和毫发无损返回同样仍待游戏内验证。

三场战斗内部标题为 `Edward vs. Undead King`、`Bel'Kara vs. Conclave`、`Katzok vs. King William`，未包含在当前英文properties键集合中。本批只翻译现有通用资源，不修改XML、战场文件或独立战役文本，也不宣称这些内部标题已汉化。

## 验证与状态

- 新键与选定源文本集合一致；源键、重复键、占位符及次数、HTML、换行标记、编码和命名空间检查通过。
- XML检查覆盖309组通用对话、273个对话关联选项、213个地点选项、24个回调及106个后续关卡。独立战役对白依赖仍为30组。
- Java成功解码6,722条；四种字体样式覆盖译文、引擎符号及1,402条英文回退。
- 既有可编辑译文与运行时键值保留；主消息和战役运行时逐字节不变，保留字体修复及用户确认的术语。
- 简介只更新分类进度；双语战役段落保持不变，不添加挑战或剧情细节。结果见 `inspection/shared-batch20-validation.json`。
- 未发现需要新增到问题日志的已确认故障。

第18–20批尚未同步模组文件夹。本批未提交、推送或上传Steam，游戏内测试继续暂缓。
