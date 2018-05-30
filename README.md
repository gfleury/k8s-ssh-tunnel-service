# SSH Tunnel as a Kubernetes Service

Creates a Kubernetes Service/Deployment/ConfigMap allowing to have SSH tunnels as Kubernetes services. 
For development environments with Kubernetes. 


## Example:
Run:

```
$ ssh-client.py 3306:internal-mysql.example.com:3306 admin@bastion-host.example.com ~/.ssh/id_rsa ssh-tunnel-service-mysql
$ kubectl apply -f ssh-tunnel-service-mysql.yaml
```

Next step your Kubernetes cluster should have a service available with the hostname `ssh-tunnel-service-mysql.svc.cluster.local` listening to the port 3306.


# Licence
MIT


