# 血与月独立对白第1批：完整文件

2026-11-21。新增 `translation/werewolfdlc-conversations-zh.properties`，以 `aof3-werewolf-dlc` 中的英文properties、对白XML、关卡与战场文件为依据，完整翻译21组130条内容（65条角色名、65条台词），另有2条元数据。

## 范围

| 完整对白组 | 内容键数 |
| --- | ---: |
| W01_Footman_death | 2 |
| W01_Knight_damage | 4 |
| W02_Dwarves_battle_intro | 14 |
| W02_Forest_battle_intro | 10 |
| W02_Knight_death | 2 |
| W02_Monk_damage | 4 |
| W02_RoyalGuard_damage | 4 |
| W03_Arges_death | 2 |
| W03_Brontes_damage | 2 |
| W03_Gats_death | 2 |
| W04_NagaWarrior_damage | 2 |
| W04_Octopod_death | 2 |
| W05_Necromancer_death | 6 |
| W05_Shella_control | 8 |
| W05_Shella_damage | 8 |
| W05_Shella_death | 6 |
| WXX_Dwarves_Gats_death_hint | 8 |
| WXX_Dwarves_necromancers_hint | 8 |
| WXX_Forest_Gats_death_hint | 14 |
| WXX_Forest_necromancers_hint | 18 |
| WXX_Welcome | 4 |

七组关卡调用对白共76条，14组战斗反应共54条。文件达到130/130（100%），构建要求完整源键集。此前通用第26–28批的251条狼人关卡文本保持不变，不新增重复的 `werewolfdlc-zh.properties`。资源条目覆盖率不等于全文字数、全游戏或全部脚本动态文本完成率。

## 文风与关系

沿用冈瑟、谢拉、古尔卡尔等既有译名。吉尔洛克的荣誉观、芬的调侃与奈丽／巴尔瓦的拌嘴各自保留；矮人口语不添加地方口音。芬对血红色的笑话、冈瑟对章鱼的寿司玩笑均按原文译出，不删改黑色幽默。

谢拉是冈瑟的妻子，相关称呼按夫妻关系处理，不把girl误写成女儿。保留她无法摆脱控制的犹疑和救女儿时被打断的呼喊，不宣称控制成功或复活。冈瑟的咆哮沿用“吼——！”。本批没有具名地点，普通沼泽不另造专名。

## 关联核对

- 21份对白XML的角色、台词和索引均与资源对应；无新增选项引用、命令或纯图片空索引。
- 欢迎提示在01调用；05a按矮人／森林战役播放对应战前对白；12和17退出时分别按战役播放两套线索提示，共七处调用。所有条件保持原样。
- 五个战场中核对14个完整序列化对白名称：W01_Hunters两组、W02_Wolf_in_Distress三组、W03_Gats三组、W04_Nagas_Temple两组、W05_Reunion_in_Death四组。仅确认名称引用存在，不推断具体伤害阈值、控制机制或实际触发次序。
- 保留既有通用资源的剧情分支、谢拉移除脚本差异和冈瑟招募选项；未改奖励或角色状态，相关历史核对见通用第26–28批。

## 验证与交付

构建、完整源键集、原文归档一致性、HTML和编码检查通过。Java解码8,313条运行时条目，四种字体样式及引擎符号覆盖通过；本文件缺键回退为零，所提供参考的481条英文回退仍来自亡灵战役。物品页布局夹具保持497/500像素，面板590×467。

此前76份可编辑properties和八份运行时properties逐字节不变。简介只新增血与月独立对话文件进度，保持简洁、无剧透与双语战役名。详见 `inspection/werewolf-dialogue-batch1-validation.json` 及扩展验证报告。本批未安装、提交、推送或上传Steam，游戏内测试继续暂缓；自动检查不证明实际布局与触发行为。
