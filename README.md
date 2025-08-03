![logo](https://s3.amazonaws.com/vipm-io-media-files-production/media/package-list-images/7d7747a7-68b1-4cd7-9527-19eb96be9d7c.png)
## Graduation Project

> - Technologies used:
> - Flask
> - Ansible
> - Jenkins
> - Prometheus
> - Flake8
> - Alertmanager

---

___A little about my project: This project delivers end-to-end infrastructure automation
using Ansible as the IaC backbone. It deploys Jenkins with JCasC (Configuration-as-Code)
for zero-touch setup, establishes Prometheus/Alertmanager monitoring, and manages Flask
applications. When code updates hit Git repositories, Jenkins auto-triggers pipelines that:
pull the latest code → run linters and unit tests → execute Ansible playbooks for zero-downtime
Flask redeploys → reconfigure monitoring → send Telegram deployment alerts via Alertmanager
– creating a fully automated CI/CD loop with quality gates and real-time observability.___

---

## How to install project: 

1. Copy project repository.

```bash
git clone https://github.com/nuclear77/theGP.git
```
2. Copy app repository.
```bash
git clone https://github.com/nuclear77/PG.git
```

3. Change working directory.

```bash
cd ~/PycharmProjects/theGP/project/ansible
```

4. Launch project:

```bash
ansible-playbook playbook.yml -i inventori.ini --ask-vault-pass
```

---
### application repository [on this link](https://github.com/nuclear77/PG) 

## Main paths

| Service      | URL                    |
|--------------|------------------------|
| FLask app    | http://localhost:6060/ |
| Jenkins      | http://localhost:8080/ |
| Prometheus   | http://localhost:9090  |
| Alertmanager | http://localhost:9093/ |