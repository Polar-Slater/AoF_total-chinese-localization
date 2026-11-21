# 海盗独立对白第1批：14组剧情对白

2026-11-21。继续独立扩展对白，新增 `translation/piratesdlc-conversations-zh.properties`。英文基线为 `source/aof-pirates-dlc/piratesdlc-conversations-en.properties`，对白与关卡定义对照同一原始归档，不新增重复的 `piratesdlc-zh.properties` 关卡资源。

## 范围

| 完整对白组 | 内容键数 |
| --- | ---: |
| PXX_Welcome | 4 |
| PXX_Human_intro | 36 |
| PXX_Undead_intro | 32 |
| PXX_Tavern_drunkard | 8 |
| PXX_Tavern_round | 2 |
| PXX_Human_treasure | 22 |
| PXX_Undead_treasure | 24 |
| PXX_Human_postgame | 34 |
| PXX_Undead_postgame | 30 |
| PXX_IslandSearch_failure | 4 |
| PXX_IslandSearch_success | 4 |
| PXX_MerchantShip_enter | 10 |
| PXX_Executioner_select | 11 |
| PXX_Congratulations | 8 |
| 合计 | 229 |

新增229条内容、2条元数据，文件覆盖229/239（95.8%）。余下 `P02_Pikeman_death`、`P03_Gargoyle_damage`、`P04_Executioner_damage`、`P05_NagaWarrior_damage` 四组共10条战斗反应继续回退英文。内容条目包括角色名、台词和选择页，不是字数统计或整个扩展完成率。

## 文风与术语

沿用红胡子船长、克里尔、威廉国王和黑卫士城堡 (Black Guard Castle)。Lucifer暂译路西法，不凭一句提及推断身份。醉酒水手与醉汉按原角色标签分别译名，刽子手保留原泛称，不擅自替换成通用关卡中的赛拉斯。

骑士的礼貌与讽刺、克里尔的蔑视与心声分开处理，保留原文地图拿反的情节、船长对船的拟人化称呼及酒鬼的胡话。两条路线中重复原句统一译法。财宝指战利品，不套用界面资金；老兵指单位资历。扩展祝贺页保留原游戏产品名称，不把旧作名称改为Total。

## XML与关联核对

14组的所有角色名、台词与选择文本逐项对应原XML；没有纯图片空索引。全部14处关卡调用均可定位，人类／亡灵条件、状态1/2/3/9、丛林搜索标记及商船入场保持原样。请客叙述对应已有扣除100金币的选项，不写成免费服务。

刽子手选择页的两处引用均指向 `LevelPiratesExecutioner01`：逃跑执行 `noop-final`，结束当前交互；迎战先将任务状态设为9，再进入 `LevelPiratesExecutioner02`。目标关卡的八条通用文本已覆盖，仍保留其人物专名与顺序。检查器逐项比较已审核命令列表，任何改动都需重新核对，不将所有非跳转命令一律放行。

战斗胜利命令给予全队经验、金币，播放祝贺对白并返回世界地图；失败使用既有 `${defeat-level-name}`。不改奖励、选项或脚本。已有BUG-003夜袭任务条件差异仍见问题记录，本批没有用改译掩盖该问题。

## 验证与交付

构建、原文键、HTML标签顺序、英雄变量及完整组检查通过。14份对白XML、14处调用与两个选项检查通过。Java解码8,151条运行时条目，四种字体样式和引擎符号覆盖通过；所提供参考的英文回退为491条（亡灵481、海盗10）。物品页布局夹具保持497/500像素，面板590×467。

之前74份可编辑properties、六份运行时properties逐字节不变；正文4,215条、通用文件3,163条、亡灵战役251条及永生之旅275条均保持原覆盖。简介仅新增海盗独立对话文件进度，保留双语战役名、简洁无剧透格式。详见 `inspection/pirates-dialogue-batch1-validation.json` 及两个扩展验证报告。

本批尚未安装、提交、推送或上传Steam；游戏内测试继续暂缓。自动检查不证明对白宽度与实际触发行为。
