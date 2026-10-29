# Security milestone: Public credential check

**Record date:** 2026-10-29. Exact commit timestamps are available from linked Git history.

## Changes
- Added `tools/check_public_secrets.py` to inspect Git-tracked text files for several high-confidence credential patterns.
- Added `.github/workflows/public-credential-hygiene.yml` to run on pull requests, pushes to main, and manual dispatch.
- Workflow requests read-only repository contents permission, disables persistent checkout credentials, and never uploads the contents of detected credentials to its logs.
- Existing branches, source history and repo visibility are unchanged.

## Scope and limitations
- This lightweight check does not replace GitHub secret scanning, push protection or full code scanning.
- It cannot find every credential type, a secret in untracked files, or past commits not in the checked-out tree.
- The workflow has been committed, but successful execution and whether GitHub Actions is enabled have not yet been confirmed. Owner must inspect the Actions run.
- No claim is made that the private development repositories have been fully scanned.
- A triggered pull-request run reports findings; it does not enforce merge blocking unless a matching required status check is selected in repository rules.

## Evidence
- Scanner commit: `4220d96a0f7280d2d763ec718ed4a805d9d67dac`
- Workflow commit: `1e5e2d2ef3b9a99882341cdef5f02d4e48ebc4fe`

## Next validation
Check the newest `Public credential hygiene` Actions run; if successful, add that exact check as a required status check to the public ruleset if it does not disrupt sole-maintainer development.
