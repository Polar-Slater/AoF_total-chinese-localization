# 永生之旅独立对白第2批：战斗反应

2026-11-21。按用户指定范围完成剩余九组战斗反应，共34条内容键（17条角色名、17条台词），不改动此前175条对白或其他资源译文。

## 范围与统计

| 完整对白组 | 内容键数 | 战场资源 |
| --- | ---: | --- |
| A01_ChaosSpawn_damage | 2 | A01_WellOfWishes |
| A01_Fiend_death | 2 | A01_WellOfWishes |
| A02_Spider_damage | 4 | A02_ForgottenMine_I |
| A02_WaterElemental_activation | 2 | A02_ForgottenMine_II |
| A02_WaterElemental_death | 4 | A02_ForgottenMine_II |
| A02_Lich_damage | 10 | A02_ForgottenMine_III |
| A02_Skeleton_death | 2 | A02_ForgottenMine_III |
| A03_RedCrab_damage | 4 | A03_Crab_Cave |
| A03_RedCrab_death | 4 | A03_Crab_Cave |
| 合计 | 34 | 五个战场 |

`alchemistdlc-conversations` 累计209/275条内容（76.0%），共23个完整对白组、2条元数据。余下七组回归游戏提示共66条继续回退英文，不属于本次委托。主消息4,215条、通用文件3,163条、亡灵战役251条保持不变；全项目运行时共7,854条（含元数据）。此进度为资源条目覆盖率，不是整部扩展或全游戏完成率。

## 原文与语气

- 对照 `aof-alchemist-dlc` 归档中的英文properties及九份对白XML，保留所有角色、顺序、HTML标签与四处显式换行。
- Marth使用既有译名玛尔斯；不因资源键含Lich而改掉原文的角色专名。沿用塔尔尼斯、水元素、蟹神。
- 保留塔尔尼斯的夸张、怕蜘蛛和嘴硬，承接“付出代价／不给酒钱”的笑话、酒馆姑娘的暗示及未说完的粗口；水元素的咕噜声与下一句嘲讽使用同一拟声词。
- 蟹钳威胁保留“矮一个脑袋”的黑色幽默。未新增地名、奖励、触发条件说明或脚本文本。

## 关联和验证

九组对白不由世界地图关卡XML直接调用，而在五份 `.brd` 战场文件中引用。覆盖声明新增 `board_conversations`；检查器解压BAT-ZIP数据，确认Java序列化流中存在完整的对白名称字符串，不执行反序列化或游戏代码。此检查证明资源名称关联存在，不证明单位归属、触发时机、伤害阈值或游戏内实际表现。

构建及扩展XML检查通过：累计23组、209条内容、两个既有选项引用、五个纯图片索引和九个战场名称引用。英文参考与原始归档一致。四处HTML换行及先前选择页结构保持不变。

Java检查解码7,854条运行时条目，四种字体样式与引擎符号检查通过；所提供参考文件的547条英文回退中，亡灵战役481条、本扩展66条，正文与两个通用文件均为零。物品页布局夹具通过：497/500像素，物品面板590×467。

此前175条扩展对白逐键保留，其他73份可编辑properties及五份运行时properties逐字节不变。简介只更新本文件的进度数字，保留简洁格式及全部双语战役名。验证记录见 `inspection/alchemist-dialogue-batch2-validation.json`、`inspection/expansion-validation.json` 和 `inspection/expansion-xml-validation.json`。

本批未同步到模组文件夹，未提交、推送或上传Steam；游戏内测试按用户要求继续暂缓。
