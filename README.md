## Graduation Project

> - Technologies used:
> - Flask
> - Ansible
> - Jenkins
> - Prometheus
> - Flake8

---

1. First step change directory

```bash
cd ~/PycharmProjects/theGP/project/ansible
```

2. Choices to launch project:

> Without monitoring
```bash
ansible-playbook playbook.yml \
    -i "localhost," \
    --connection=local \
    -e "app_source_dir=${HOME}/PycharmProjects/theGP/project/app" \
    -e "ansible_template_dir=${HOME}/PycharmProjects/theGP/project/ansible/templates" \
    -e "app_port=6060"
```

> With monitoring 

```bash
ansible-playbook playbook-monitoring.yml \
    -i "localhost," \
    --connection=local \
    -e "prometheus_config_dir=${HOME}/PycharmProjects/theGP/project/monitoring" \
    -e "app_port=6060"
```

3. Receiving Jenkins admin password:

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

---

## Main paths

| Service    | URL                    |
|------------|------------------------|
| FLask app  | http://localhost:6060/ |
| Jenkins    | http://localhost:8080/ |
| Prometheus | http://localhost:9090  |