## Intro to Kubernetes

#### Pod

**Replicaset**: Ensures that there's x number of duplicates of the pod

#### **Deployment**

- In most cases deployment = replicaset
- When deployment is deleted, repliaset and pods in the deployment are also deleted

| Deployment                                                   | Replicaset |
| ------------------------------------------------------------ | ---------- |
| - Focused on **distribution**<br />- Can **version control** and update<br />- Can manage different versions |            |

**Version Control**

- `--record`: leaves the versionof the deployment

**Namespace**

#### **Configmap**

Create configmap: `kubectl create configmap --[OPTIONS]`

- Ex. `kubectl create configmap log-level-configmap --from-literal LOG_LEVEL=DEBUG`
- Ex. `kubectl create configmap start-k8s --from-literal k8s=kubernetes --from-literal container=docker`

List configmap

- `kubectl get configmap`
- `kubectl describe <configmap_name>`

Show configmap in yaml: `kubectl get configmap log-level-configmap -o yaml`



#### **Utilizing configmap**

**METHOD 1: Storing configmap into an environment variable**

1. Create yml file: `vi all-env-from-configmap.yml`

   ```bash
   apiVersion: v1
   kind: Pod
   metadata:
     name: container-env-example
   spec:
     containers:
       - name: my-container
         image: busybox
         args: ['tail', '-f', '/dev/null']
         
         # defining environment variables
         envFrom:
           - configMapRef:
               name: log-level-configmap
           - configMapRef:
               name: start-k8s
   ```

2. Create the pod: `kubectl apply -f all-env-from-configmap.yml`

3. Check whether the pod has been created: `kubectl get pods`

4. Check whether environment variables have been properly passed off: `kubectl exec container-env-example -- env`

**METHOD 1.1: Set selected key-value pairs as env variable (to assign a name to env var)**

1. Create a yml file: `vi selective-env-from-configmap.yml`

   ```bash
   apiVersion: v1
   kind: Pod
   metadata:
     name: container-env-example
   spec:
     containers:
       - name: my-container
         image: busybox
         args: ['tail', '-f', '/dev/null']
         env:
           - name: ENV_KEYNAME_1                
             valueFrom:                                                                     
               configMapKeyRef:                                                             
                 name: log-level-configmap     
                 key: LOG_LEVEL                
           - name: ENV_KEYNAME_2
             valueFrom:
               configMapKeyRef:
                 name: start-k8s
                 key: k8s
   
   ```

   

**METHOD 2: Mount the configmap values internally**

1. Mount all the key-value pairs to the pod (in the yml file): `vi volume-mount-configmap.yml`

   ```bash
   apiVersion: v1
   kind: Pod
   metadata:
     name: configmap-volume-pod
   spec:
     containers:
       - name: my-container
         image: busybox
         args: ["tail", "-f", "/dev/null"]
         
         # defining mounting destination of the volume created
         volumeMounts:
           - name: configmap-volume
             mountPath: /etc/config
             
     # defining the volume        
     volumes:
       - name: configmap-volume
         configMap:
   				name: start-k8s
   ```

   

2. Create pods: `kubectl apply -f volume-mount-configmap.yml`
3. Check what's been created
   1. Check whether the pods have been created: `kubectl get pods`
   2. Check /etc/config directory: `kubectl exec configmap-volume-pod -- ls -l /etc/config`
   3. Check file contents: `kubectl exec configmap-volume-pod -- cat /etc/config/container`, `kubectl exec configmap-volume-pod -- cat /etc/config/k8s`
      1. Keys are stored at the end of the path: `container`, `k8s`
      2. Values are returned when running this code: `docker`, `kubernetes`

#### Secret

- Types of Secret
  - Opaque: Default secret type; save the user given data as the secret value `kubectl create secret generic`
  - TLS: Used to sore public and private key for TLS connection (Usually for the security purpose of the applications within pods)
- Create secret: `kubectl create secret generic my-password **--from-literal** password=1q2w3e4r`
- 