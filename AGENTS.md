# Repository conventions

- Use **Creative Ad Director** for the product/display name and `creative-ad-director` for the skill identifier, directory, and package prefix.
- Keep the English and Chinese READMEs, UI metadata, import package, and usage instructions consistent with the current skill.
- After each authorized modification, run the relevant validation and rebuild the import ZIP when its source files change. Commit and push the completed changes to `https://github.com/XianlinLu/Creative-Ad-Director` and integrate them into the default branch unless the user requests another destination. A local-only edit or an unmerged draft PR is not the final delivery for this repository.
- Preserve unrelated concurrent changes; never force-push or rewrite repository history to perform a rename. If remote updates prevent a safe push, reconcile them before reporting completion.
- Report the resulting commit or PR and distinguish static validation from actual Lumina generation tests.
