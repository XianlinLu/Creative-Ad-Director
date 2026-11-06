# Meme Merchant

[简体中文](README.zh-CN.md)

Meme Merchant is a Lumina Canvas skill for turning a product URL, product media, or a short selling brief into evidence-grounded, funny, conversion-focused short ads. It adapts the artifact-first, native-review, production, and editable-delivery discipline of [Cinema-Craft](https://github.com/XianlinLu/Cinema-Craft) to ecommerce performance creative.

The workflow includes product-page research, recovery when webpage images cannot be inspected, white-model/product identity locking, three-direction creative development, comic short-form scripts, modular hook/CTA variants, native Lumina generation, editable Video Editor finishing, claim checks, and verified exports.

## Install in Lumina

Download `dist/lumina-meme-merchant-v0.1.0.zip`, extract it, and import `SKILL.md`, `agents/`, and `references/` into a new Lumina skill. The ZIP intentionally excludes repository-only scripts and tests.

Example prompt:

> Use this product URL to make a 15-second 9:16 funny ecommerce ad. Keep the product and claims accurate, create three hook options, and deliver one master plus two hook variants.

## Repository layout

```text
skills/lumina-meme-merchant/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
tests/
dist/
```

## Validate and build

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/lumina-meme-merchant
python3 skills/lumina-meme-merchant/scripts/preflight.py
python3 -m unittest discover -s tests -v
python3 skills/lumina-meme-merchant/scripts/build_skill.py \
  --output dist/lumina-meme-merchant-v0.1.0.zip
```

Static checks validate packaging and instruction integrity. Actual URL access, paid generation, native Question cards, Video Editor behavior, policy review, and end-to-end exports still require testing in the active Lumina environment.
