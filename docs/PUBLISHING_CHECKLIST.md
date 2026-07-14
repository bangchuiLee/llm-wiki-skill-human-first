# Public Release Checklist

1. Confirm every file is original work or has a documented compatible license.
2. Keep `LICENSE`, `THIRD_PARTY_NOTICES.md`, and all third-party license texts unchanged.
3. Review `git status --ignored` and `git diff --cached` before every push.
4. Confirm no vault content, external source file, browser capture, profile, cache, credential, URL with private parameters, or personal path is staged.
5. Run the tests:

   ```powershell
   D:\python\python.exe scripts\tests\test_validate_reading_contract.py -v
   ```

6. Run the source-registry validation in a Bash-compatible shell:

   ```bash
   bash scripts/source-registry.sh validate
   ```

7. Publish the repository as `llm-wiki` with the MIT license for original material only. Do not describe optional upstream adapters as bundled dependencies.
