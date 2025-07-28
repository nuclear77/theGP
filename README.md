## Graduation Project

> - Technologies used:
> - Flask
> - Ansible
> - Jenkins
> - Prometheus
> - Flake8
> - Alertmanager

---

1. First step change directory

```bash
cd ~/PycharmProjects/theGP/project/ansible
```

2. launch project:

```bash
ansible-playbook playbook.yml -i inventori.ini --ask-vault-pass
```

3. Receiving Jenkins admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## Main paths

| Service      | URL                    |
|--------------|------------------------|
| FLask app    | http://localhost:6060/ |
| Jenkins      | http://localhost:8080/ |
| Prometheus   | http://localhost:9090  |
| Alertmanager | http://localhost:9093/ |