# 翻译过程中发现的游戏问题

更新：2026-11-17。适用版本：Age of Fear: Total v11.0.5。

集中记录翻译期间发现的原版脚本错误、原文矛盾、本地化兼容问题和待调查报告。静态脚本证据与游戏内复现分别记录；“中文显示已修正”不代表原版程序或英文资源已修复。后续发现沿用编号追加，修复后保留记录。

## 问题总表

| 编号 | 问题 | 类型 | 当前状态 |
| --- | --- | --- | --- |
| BUG-001 | 萨满净化菜单与命令指向不同英雄 | 原版脚本 | 静态确认；运行影响待复现 |
| BUG-002 | 灵魂之井重复调用献祭对话 | 原版脚本 | 静态确认；重复显示待复现 |
| BUG-003 | 海盗夜袭任务要求潜海者却检查元素生物 | 原版任务条件 | 静态确认不一致；奖励触发待复现 |
| TXT-001 | 头盔升级价格与材料说明错误 | 原版显示文本 | 中文已按脚本修正；原版未改 |
| TXT-002 | 方尖碑数量及破坏后的叙述矛盾 | 原版叙事 | 已确认原文不一致；部分保留 |
| TXT-003 | 灯神对白中的愿望数量不一致 | 原版叙事 | 已记录；是否刻意安排待核实 |
| TXT-004 | 修道院祈祷选项进入草药店伏击叙述 | 原版分支与叙述 | 静态确认不一致；游戏内表现待复核 |
| LOC-001 | 中文数字仍按英文规则拼接 | 引擎本地化限制 | 已通过格式化探针确认；未修复 |
| LOC-002 | 小游戏脚本直接生成英文 | 资源外文本 | 已确认；尚未本地化 |
| LOC-003 | 旧字体缺少提示符号 | 字体兼容 | 已换字体并自动验证；保留历史记录 |
| LOC-004 | 物品仓库两栏挤缩、属性截断 | 字体与固定布局兼容 | 模组缓解方案已安装；完整界面复测待办 |
| REP-001 | `UXX_Please_review_us` 加载警告 | 待调查报告 | 根因未定 |
| REP-002 | Workshop Manager 上传返回 `InvalidParam` | 待调查报告 | 历史截图；根因未定，后来有成功上传反馈 |
| RES-001 | 沙虫开放战役缺少对应properties资源 | 资源覆盖缺口 | XML有文本；本地化接入方式待核实 |

## 原版脚本问题

### BUG-001 萨满净化目标不一致

- **证据位置：** `aof-data.zip` 内 `com/aof/resource/campaign/level/shared/shared-shamanhut.xml`，`LevelShamanHut01` 的 `on-select-42`。
- **静态事实：** 按钮使用 `${hero-107-name}`，可用条件检查英雄107的类型和诅咒物品；扣除200金币后却执行 `unequip-items-cursed ${hero-17-id}`。其余35项服务的目标索引一致。
- **可能影响：** 选择英雄107的服务时可能作用于英雄17，或扣费后未处理预期目标。具体表现尚未实测。
- **处理：** 未改脚本，也未将中文按钮改成英雄17来掩盖错误。后续使用备份存档检查两名英雄的物品与扣费结果，再向原作者报告目标索引问题。
- **记录：** [第16批](batches/SHARED-EVENTS-BATCH16.md)。

### BUG-002 灵魂之井重复播放命令

- **证据位置：** `aof-data.zip` 内 `com/aof/resource/campaign/level/shared/shared-soulswell.xml`，`LevelSoulsWell02` 的 `on-function-3`。
- **静态事实：** 非空单位选择先调用 `SXX_SoulsWell_sacrifice`，随后在非矮人战役再次调用同一对话；矮人战役则追加 `DXX_SoulsWell_sacrifice`。
- **可能影响：** 非矮人战役可能重复显示通用献祭对白；矮人战役会排入通用和专属两组对白。命令重复已确认，最终显示行为尚待验证。
- **处理：** 原脚本与译文均保留。后续分别检查矮人及其他战役，确认是否需要删除或限制第一条播放命令。
- **记录：** [第15批](batches/SHARED-EVENTS-BATCH15.md)。

### BUG-003 海盗夜袭任务的目标种族不一致

- **证据位置：** `aof-pirates-dlc.zip` 内 `com/aof/resource/campaign/level/shared/piratesdlc.xml`，`LevelPirates17` 的 `on-battle-task-1`。
- **静态事实：** 英文提示为 `Gold Bar: Kill all Divers before turn eight`，条件却为 `(${battle-enemy-race-Elementals-count}=='0')AND(${battle-turn-number}LESS_EQUAL_8)`，奖励是一个 `GoldBarItem`。`aof-data.zip` 中 `seadiver.xml`、`seadiverfisher.xml`、`seadiverwarrior.xml` 的种族均为 `Divers`，与 `Elementals` 不同。
- **可能影响：** 任务奖励可能按元素生物而非潜海者的剩余数量触发；是否提前发奖、是否有其他战场条件影响，需要用备份存档复现。仅确认XML条件与提示／单位定义不一致，不声称已观察到实际奖励错误。
- **处理：** 中文仍按原文写“消灭所有潜海者”，未改成元素生物来掩盖问题，也未修改游戏脚本。后续分别检查两类单位存活时的任务状态及金锭获得时机，再决定是否向原作者提交修复建议。
- **记录：** [第30批](batches/SHARED-EVENTS-BATCH30.md)。

## 原文显示与叙事问题

### TXT-001 符文锻造师头盔升级说明

`shared-runesmith.xml` 中 `LevelRuneSmith01.on-select-6` 的按钮写500金币，说明写400金币，并把输入物品误写成 Quality Armour。脚本检查并扣除400金币，将 `QualityHelmetItem` 换成 `HelmetOfHasteItem`。

中文按钮和说明已统一为“精制头盔 → 迅捷头盔，400金币”。游戏价格、交换逻辑及英文原文未修改。见[第12批](batches/SHARED-EVENTS-BATCH12.md)。

### TXT-002 魔力方尖碑叙事矛盾

`shared-manasource.xml` 的 `LevelManaObelisks01/02` 及 `SXX_ManaObelisks_gain` 对应文本存在两项矛盾：地图名为 Four Obelisks，结果却提到三座；结果称方尖碑炸裂，后续地点却仍描述它们与离开时相同。

中文结果使用“这些魔法造物”避免数量冲突，但保留后续叙事，没有编造重建过程。调试选项只给予6枚碎片，而触发门槛为7枚；这是一项调试配置差异，暂不认定为正式玩法错误。见[第13批](batches/SHARED-EVENTS-BATCH13.md)。

### TXT-003 灯神愿望数量

灯神事件许愿前提到一个愿望，入队对白又提到三个愿望。差异来自原文，是否属于角色台词或旧版本遗留尚未确定。译文保留原意，不据此改动愿望规则。定位范围为 `SXX_DjinLamp` 相关对话；见[第8批](batches/SHARED-EVENTS-BATCH8.md)。

### TXT-004 祈祷入口与草药店叙述不一致

`shared-vampiremonastery.xml` 中 `LevelVampireMonastery01.on-select-2`（到礼拜堂祈祷）和 `on-select-3`（拜访草药师店铺）都在 `${date-hour}LESS_THAN_4` 时跳转 `LevelVampireMonastery03b`。然而该段原文明确叙述英雄前往草药师店铺、刚跨入店门便撞见仪式，不能直接衔接祈祷选项。

两个入口共享伏击可能是设计意图；已确认的问题限于选项与叙述衔接，不据此断言时间判定错误。中文保留原意，未修改选项目的地或脚本。后续分别从两种入口复现，再考虑由原作者拆分或改写共用介绍。见[第24批](batches/SHARED-EVENTS-BATCH24.md)。

## 本地化兼容问题

### LOC-001 中文数字拼接

`StringHelper.numberToString` 的实际探针结果包括21 → “二十 一”、101 → “一 百 一”、10,000 → “十 千”。引擎仍采用空格和千进位分组，不能单靠数字词properties实现中文的补零及万／亿分组。当前保留正确数量级，不以错译替代引擎修复。后续应在格式化逻辑层处理。见[正文第8批](batches/MAIN-TEXT-BATCH8.md)。

### LOC-002 脚本生成的英文片段

猜杯子脚本把 `game-cups-result` 直接设为 `first/second/third`；纸牌换牌与牌型标签、轮盘部分组合也有XML直接生成的英文。当前翻译保留变量，必要时给出中文对应提示。这些片段不因properties文件覆盖率上升而自动汉化。后续需盘点脚本文本并确认可维护的本地化方式。见[通用文本50%记录](batches/SHARED-TEXT-50-PERCENT.md)。

### LOC-003 字体缺字

旧SimHei配置不能完整覆盖引擎提示中的U+00A0及U+2022等字符。已替换为静态常规字重Noto Sans SC；按钮随后使用AoF Han UI派生字体。Java检查覆盖译文、英文回退、引擎符号及四种字体样式。用户曾反馈更新后的版本正常，但不据此宣称所有屏幕均已逐项检查。见[测试指南](TESTING.md)。

### LOC-004 物品仓库布局挤缩

用户截图显示角色和物品栏挤在中央。字体度量与独立Swing夹具确认：固定500像素高的布局中，物品列表加资金标签需要502像素，触发布局缩窄。紧凑行高的AoF Han UI将其降至497像素；夹具检查通过，模组字体配置已安装。

这是本地化字体与游戏固定布局的兼容问题，未证明原版默认字体下也会发生。游戏程序未修改；重启后的完整物品仓库画面仍待确认。详细证据和验证边界见[布局修复记录](batches/INVENTORY-LAYOUT-FIX.md)。

## 待调查报告与资源缺口

### REP-001 对话加载警告

早期验证记录出现 `UXX_Please_review_us` 无法加载的警告。尚未确定资源来源、触发条件和根因。后续保留完整日志，核对归档内对话定义及引用关系，再判断是原版资源、版本差异还是模组问题。不新增虚构对白或删除触发来隐藏警告。见[测试指南](TESTING.md)。

### REP-002 Workshop Manager InvalidParam

用户历史截图显示 `Cannot update item. Error: Workshop Item not updated. Error: InvalidParam`。截图没有给出具体失败字段，不能据此认定是简介长度、格式或所有者字段导致。用户后来报告上传成功，尚无可重复的故障条件。

保留为历史报告。若再次发生，记录管理器版本、上传日志和失败前后的配置差异；日志留在本地并去除账号信息后再分享。目前不宣称已找到或修复根因。

### RES-001 沙虫开放战役资源缺口

2026-11-17盘点发现：`data/aof-total.zip` 内有 `com/aof/resource/campaign/owsandwormcampaign.xml`，包含标题、简介、开场、选项和失败文本；当前提取的英文资源中没有 `owsandwormcampaign-en.properties` 或对应对话properties。

记录为翻译接入缺口，不判定战役不可玩或引擎无法加载。后续核对本地化键导出规则及运行时查找方式，再建立资源基线；未找到properties不能记作“0条，已完成”。

## 后续维护

新增记录应包含发现版本、资源键或触发器、实际证据、预期与实际差异、复现状态、翻译影响及下一步。修复时注明改动的是译文、模组资源还是游戏逻辑，并分别记录自动验证、安装和游戏内复测状态。排版截图或源码疑点不足以证明原版玩法故障时，保持“待调查”分类。
