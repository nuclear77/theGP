## Project with Ansible-roles and CI/CD pipline

> commands to use
```bash
cd ~/PycharmProjects/theGP/project/ansible
```

```bash
ansible-playbook playbook.yml     -i "localhost,"     --connection=local     -e "app_source_dir=${HOME}/PycharmProjects/theGP/project/app"     -e "ansible_template_dir=${HOME}/PycharmProjects/theGP/project/ansible/templates"
```

```bash
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
```

- Flask to http://localhost:6060/
- Jenkins to http://localhost:8080/