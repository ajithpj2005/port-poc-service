# port-poc-service

Sample Flask service used for a [Port](https://www.port.io) proof of concept.

## What this repo demonstrates

| Port capability | How it shows up here |
| --- | --- |
| Software catalog | Port's GitHub integration syncs this repo as a `githubRepository`; it is linked to the `port-poc-service` **Service** entity. |
| Jira linkage | Jira issues labelled `service:port-poc-service` are related to the Service in Port. |
| Scorecards | The **Production Readiness** scorecard checks README, `.gitignore`, PR template, language, team, criticality, recent activity and CODEOWNERS. |
| Self-service | The Port workflow **Add CODEOWNERS** dispatches `.github/workflows/add-codeowners.yml`, which commits a `CODEOWNERS` file and lifts the service to Gold. |

The repo intentionally ships **without** a `CODEOWNERS` file so the self-service action has something to fix.

## Run locally

```bash
pip install -r requirements.txt
python -m src.app      # http://localhost:8080/health
pytest -q
```
