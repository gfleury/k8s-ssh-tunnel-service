#!/usr/bin/env python
import sys
from jinja2 import FileSystemLoader, Environment

def render_from_template(directory, template_name, **kwargs):
    loader = FileSystemLoader(directory)
    env = Environment(loader=loader)
    template = env.get_template(template_name)
    return template.render(kwargs)



if len(sys.argv) < 3:
     print('Use: {} PPORT:host:DPORT user@destination_host ssh_private_key_file k8s_service_name'.format(sys.argv[0]))
     exit()

servicePort = sys.argv[1].partition(":")[0]

with open(sys.argv[3], 'r') as myfile:
    sshKey = myfile.read()

varsz = {
    "serviceName": sys.argv[4],
    "servicePort": servicePort,
    "sshKey": sshKey,
    "sshUserHost": sys.argv[2],
    "sshProxyParameter": sys.argv[1]
}

deployment = render_from_template("templates", "deployment.yaml", values=varsz)

with open(sys.argv[4] + ".yaml", 'w') as myfile:
    myfile.write(deployment)

