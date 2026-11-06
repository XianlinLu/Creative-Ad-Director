# Meme Market

[English](README.md)

Meme Merchant 是一个面向 Lumina 画布的电商短广告 Skill。它可以从商品 URL、商品素材或一句销售需求开始，先建立可追溯的商品证据，再创作带剧情、偏搞笑、便于拆分测试的短广告。

整体流程参考 [Cinema-Craft](https://github.com/XianlinLu/Cinema-Craft) 的“画布产物优先、原生确认、连续制作、可编辑交付”方法，并针对电商广告补充了：

- 商品页文字、结构化数据、价格/优惠、规格、FAQ、评价和素材来源分析；
- GPT 内置联网能读网页文字但未必能看网页图片时的恢复路径；
- 商品白模与 Product Lock，避免跨镜头变形、改色、乱加按键/包装文字；
- 三方向创意板、搞笑剧情、前 1.5 秒钩子、商品演示与 CTA；
- Master Body + Hook/Payoff/CTA 模块化走量版本；
- Lumina 原生生图/视频/配音/Video Editor 制作；
- 广告声称、价格优惠、评价背书、版权授权和交付前 QC。

## 导入 Lumina

下载 `dist/lumina-meme-merchant-v0.1.0.zip` 并解压，在 Lumina 中新建 Skill，导入其中的 `SKILL.md`、`agents/` 和 `references/`。ZIP 不包含仓库维护用的脚本和测试。

示例：

> 用这个商品链接做一条 15 秒、9:16 的搞笑电商广告。商品外观和卖点必须准确，先做三个开头 Hook，最终交付一条主片和两个 Hook 变体。

## 关键设计

当网页图片不能直接分析时，Skill 会区分“读到图片 URL/alt 文本”和“实际看过像素”。它会优先把官方图片通过真实可用的方式导入 Lumina 画布再验图；如果仍不可访问，就只做文本证据表和临时分镜，不会凭文件名猜颜色、Logo 或包装。只有在已有可靠参考时才建立商品白模；仅有尺寸时只能建立构图用几何块，不能冒充真实商品成片。

走量版本默认复用同一个已批准的 Body，仅替换 Hook、Payoff、CTA 或缩略图等预先规划的模块，并用清单记录每条导出的变量，避免一次把所有组合都昂贵地生成出来。

## 验证与打包

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/lumina-meme-merchant
python3 skills/lumina-meme-merchant/scripts/preflight.py
python3 -m unittest discover -s tests -v
python3 skills/lumina-meme-merchant/scripts/build_skill.py \
  --output dist/lumina-meme-merchant-v0.1.0.zip
```

静态检查只能验证结构、引用、字符上限和打包一致性；真实商品 URL 访问、付费生成、Lumina 原生卡片、Video Editor、平台广告政策和完整导出仍需在实际环境中验证。
