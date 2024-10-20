docker pull nginx
docker run nginx(image name)
docker run -d nginx(d -> detach mode)
docker ps(show running container)
docker pa -a(show all container(stopped containers))
docker start <container_name>(to start container)
docker remove <continaer_id>(to remove container)
docker run -d --name <container_name> -p 8080:80 nginx(--name specify container name, -p: tag for port mapping)
docker logs <contianer_id or name>(to check logs)
docker logs -f <contianer_id or name>(-f: to check live logs)
docker inspect <container_name>(show contianer details)
docker exec -it nc(<containername>) bash(-it: interactive, exec for execute, bash: will give terminal)
docker cp <filename> <containername>:/(to copy file into container)
docker network ls

docker build -t nau:01 .(to build docker image)

docker ex:
    FROM python:3.6-slim

    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    RUN mkdir /code
    WORKDIR /code
    RUN pip install --upgrade pip
    COPY requirements.txt /code/

    RUN pip install -r requirements.txt
    COPY . /code/

    EXPOSE 8000

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

docker compose ex:
  version: '3.8'
  services:
    myapp:
      image: nau:01
      container_name: nauapp
      ports:
        -"8080: 8081"
      volumes:
        -"/home/vishnu/music/abc.txt:/app/xyz.txt"
      environment:
        - PORT=3030
      restart: unless-stopped



=====================================================
kubernaties:


1)Features:
Container Orchestration
Automated Load Balancing
Auto Scaling
Rolling Update & Rollbacks
Service Discovery and Load Balancing
Storage Orchestration
Self-Healing
Secrets and Configuration Management
Multi-Cloud and Hybrid Cloud Support
Role-Based Access Control (RBAC)
Pods and Multi-Container Support
Monitoring and Logging

  scalability, Load Balancing, High availability, Rollout & rollback
  1. Service discovery and load balancing
  2. Storage orchestration
  3. Automated rollouts and rollbacks
  4. Automatic bin packing
  5. Self-healing
  6. Secret management

Kubernetes is an open-source platform for automating deployment, scaling, and management of containerized applications. It provides a powerful orchestration system for deploying and managing applications in clusters, making it the de facto standard for container management in production environments. Here are some of the key features of Kubernetes:

### 1. **Automated Rollouts and Rollbacks**
Kubernetes supports automated deployment and rollback processes:
   - **Rollouts**: Kubernetes gradually rolls out changes to your application or its configuration, monitoring the health of the application to ensure that it doesn't impact availability.
   - **Rollbacks**: If an issue is detected, Kubernetes can automatically roll back to a previous, stable version of the application.

### 2. **Self-Healing**
Kubernetes automatically monitors and maintains the health of your application components:
   - **Restarting Failed Containers**: It restarts containers that fail or stop unexpectedly.
   - **Rescheduling**: It replaces and reschedules containers on healthy nodes if necessary.
   - **Health Checks**: Kubernetes performs liveness and readiness probes to check the health of your application. If a probe fails, Kubernetes restarts the container or removes it from the load balancer.

### 3. **Horizontal Scaling**
Kubernetes supports both manual and automatic scaling:
   - **Horizontal Pod Autoscaler (HPA)**: Kubernetes can automatically scale the number of application instances (pods) up or down based on CPU usage, memory usage, or other custom metrics.
   - **Manual Scaling**: You can manually scale the application using a simple command like `kubectl scale`.

### 4. **Service Discovery and Load Balancing**
Kubernetes provides built-in service discovery and load balancing mechanisms:
   - **Service Discovery**: Applications do not need to know the specific IP addresses of other services. Kubernetes assigns a DNS name and a stable IP address to each service, ensuring reliable communication.
   - **Load Balancing**: Kubernetes can load-balance traffic across multiple pods, distributing incoming requests to ensure high availability.

### 5. **Storage Orchestration**
Kubernetes can manage and automate the mounting of storage systems to containers:
   - **Persistent Volumes**: Kubernetes provides a way to define storage that persists beyond the life of a pod. It supports various storage backends like local storage, cloud providers (AWS EBS, Azure Disk), and network file systems (NFS, Ceph, etc.).
   - **Dynamic Provisioning**: Kubernetes can dynamically provision storage based on the requirements defined in the Persistent Volume Claims (PVCs).

### 6. **Declarative Configuration and Management**
   - **Declarative Configuration**: Kubernetes uses YAML or JSON files to define the desired state of your application (e.g., the number of replicas, resource requirements). You can apply these configurations using the `kubectl apply` command, and Kubernetes will work to match the actual state to the declared state.
   - **ConfigMaps and Secrets**: Kubernetes allows you to manage configuration data and sensitive information separately from the application code using ConfigMaps (for configuration files) and Secrets (for sensitive data like passwords, API keys).

### 7. **Namespaces for Multi-Tenancy**
   - **Isolation**: Kubernetes supports namespaces to partition resources within a single cluster. This is useful for separating development, testing, and production environments or for managing different teams or projects.
   - **Resource Quotas**: You can set resource limits per namespace to control the amount of CPU, memory, and other resources used by each environment or project.

### 8. **Network Policies**
   - **Fine-Grained Access Control**: Kubernetes Network Policies allow you to define rules for how pods communicate with each other and with services outside the cluster. This provides an extra layer of security, ensuring that only authorized traffic is allowed between components.

### 9. **In-Built Monitoring and Logging**
   - Kubernetes integrates with monitoring and logging solutions like Prometheus, Grafana, and ELK (Elasticsearch, Logstash, Kibana) stack to provide real-time insights into cluster and application performance.
   - **Metrics Server**: Kubernetes has a metrics server that collects resource usage data (e.g., CPU and memory usage) across the cluster, which can be used for autoscaling and performance monitoring.

### 10. **Container Orchestration and Lifecycle Management**
   - **Container Scheduling**: Kubernetes schedules containers based on resource requirements and other constraints. It chooses nodes that have the required resources and affinity rules to run your pods.
   - **Stateful and Stateless Applications**: Kubernetes supports both stateful (e.g., databases) and stateless applications (e.g., web servers), providing different management patterns for each.

### 11. **RBAC (Role-Based Access Control)**
   - **Security and Access Management**: Kubernetes provides fine-grained access control through RBAC, allowing administrators to define roles and permissions for users and applications interacting with the cluster.
   - **Authentication and Authorization**: Kubernetes integrates with external identity providers and supports multiple authentication mechanisms (e.g., tokens, certificates).

### 12. **Helm Charts for Package Management**
   - **Application Templates**: Helm, the package manager for Kubernetes, allows you to define, install, and manage Kubernetes applications using Helm charts (pre-packaged application templates).
   - **Version Control**: Helm makes it easy to version and update applications, simplifying deployments and rollbacks.

### 13. **Multi-Cloud and Hybrid Cloud Support**
   - **Cloud Agnostic**: Kubernetes works across different cloud providers (AWS, Azure, GCP) and on-premises environments, providing flexibility to deploy applications in various cloud and hybrid cloud setups.
   - **Cluster Federation**: Kubernetes supports federation, allowing you to manage multiple clusters as a single entity, which is useful for disaster recovery and geographical distribution.

### 14. **Service Mesh Integration**
   - Kubernetes integrates with service mesh solutions like Istio and Linkerd to manage complex microservices architectures. These service meshes provide features like:
     - **Traffic Management**: Fine-grained control over how requests are routed between services.
     - **Observability**: Metrics, logging, and tracing for monitoring service interactions.
     - **Security**: Encryption and mutual TLS (mTLS) between services.

### 15. **Support for Batch and CI/CD Workloads**
   - **Batch Processing**: Kubernetes can manage batch workloads and cron jobs using the `Job` and `CronJob` objects, making it suitable for data processing and scheduled tasks.
   - **CI/CD Integration**: Kubernetes integrates well with CI/CD tools like Jenkins, GitLab CI, and ArgoCD, automating application builds, testing, and deployments.

### 16. **Extensibility with Custom Resources and Operators**
   - **Custom Resource Definitions (CRDs)**: Kubernetes allows you to create custom resources that extend its capabilities beyond built-in objects. CRDs are used to define new types of resources tailored to specific use cases.
   - **Operators**: Operators are custom controllers built using CRDs to manage complex stateful applications like databases (e.g., PostgreSQL, MongoDB) and messaging systems (e.g., RabbitMQ) within Kubernetes.

### 17. **Ingress Management**
   - **HTTP/HTTPS Routing**: Kubernetes provides Ingress controllers that manage external access to services, enabling HTTP and HTTPS routing with features like URL-based routing, SSL termination, and load balancing.
   - **External Traffic Control**: Ingress controllers (e.g., NGINX, Traefik) help manage how external users access internal applications, providing scalability and high availability.

### 18. **API Server and Declarative Management**
   - **API-Centric Management**: Kubernetes provides a robust API server that allows users and external systems to interact programmatically with the cluster.
   - **Declarative Configuration**: Kubernetes emphasizes declarative configuration management, ensuring that the system is continuously reconciling the desired state of applications and infrastructure.

These features make Kubernetes a powerful and flexible platform for deploying and managing modern containerized applications. Let me know if you'd like to dive deeper into any specific feature!




Master Node:
  API Server: Central communication hub and front-end for all Kubernetes operations. It validates and configures API requests and communicates with etcd to store cluster data.
  Scheduler: 
    -assign node to newly created pod
    -Determines where pods should run based on resource availability and policy constraints.
  etcd:
    -kye-value store, having all cluster data 
    -Distributed key-value store holding the state of the cluster. Acts as the single source of truth for cluster configuration and status.
  Controller Manager: 
    -responsible for managing the state of the cluster
    -Manages various controllers responsible for ensuring the cluster state matches the desired configuration.

WORKER NODE:
  Kubelet: Agent makesure that container is running in pods
  pod:
  -Single instance of running process in a cluster
  -it can run one or more containers and share the same resources
  kube-proxy: 
    -manages network traffic for services within a cluster
    -Routing traffic
      Kube-proxy forwards traffic to a service's endpoints, such as a pod or a user-provided IP address
    -Maintaining network rules
    -Implementing a virtual IP mechanism
    -Watching for changes
    -Synchronizing rules
    -Matains network rules for comm with pods
  container-runtime: A tool responsible for running containerss

Topic

Description

1. Kubernetes	An open-source container orchestration tool/system used for automating tasks like management, monitoring, scaling, and deployment of containerized applications.
2. K8s	Another term for Kubernetes.
3. Orchestration	Integration of multiple services to automate processes or synchronize information. In the context of Kubernetes, orchestration ensures seamless communication among individual containers.
4. Architecture	Understanding Kubernetes components: master node, worker nodes, etcd, API server, controller manager, and scheduler.
5. Pods:
  	The basic unit in Kubernetes, containing one or more containers.
6. Services:
  	Exposing pods to the network. Types: ClusterIP, NodePort, Load Balancer, and ExternalName.
7. Replication Controllers:
  	Ensuring a specified number of replicas of a pod are running.
8. Deployments:
  	Managing rolling updates and rollbacks.
9. ConfigMaps and Secrets:
  	Managing configuration data and sensitive information.
10. Persistent Volumes (PVs) and Persistent Volume Claims (PVCs):
  	Managing storage for stateful applications.
11. Ingress Controllers:	
  Routing external traffic to services within the cluster.
12. Helm:	
  Package manager for Kubernetes.
13. Security:	
  RBAC, Network Policies, and Pod Security Policies.
14. Monitoring and Logging:	
  Prometheus, Grafana, and ELK stack.
15. Troubleshooting:	
  Diagnosing issues with pods, services, and nodes.


8. What is a Service in Kubernetes?
The idea of the Service is to group a set of Pod endpoints into a single resource. We can configure various ways to access the grouping. By default, we can get a stable cluster IP address that the clients inside the cluster can use to contact Pods in Service.

9. How does Kubernetes manage configuration?
configmap

10. Describe the role of a Master node in Kubernetes.
Kubernetes master node components can be run within Kubernetes itself, as a set of containers within the dedicated pod. The master node is responsible for cluster management and for providing the API that is used to configure and manage resources within the Kubernetes cluster.

11. What is the role of the kube-proxy in Kubernetes and how does it facilitate communication between Pods?
The networking part of Kubernetes that enables communication between pods & services is called Kube-proxy, and it may be installed on any cluster node. Its major function is to maintain network rules for service-to-pod mapping, which provides communication to and from Kubernetes clusters.

13. What is a ConfigMap?
A ConfigMap is an API object in Kubernetes that is primarily used to store non-confidential data. ConfigMaps are a way for Kubernetes to inject configuration data into application pods, making it easier to manage and update configuration settings and assist in separating configuration from application code.

14. Describe the role of etcd in Kubernetes.
Etcd is the cluster brain that maintains records of all cluster information, which includes the desired state, the current state, resource configurations, and runtime data. It is the cluster brain that informs other processes that including the Scheduler about changes in the cluster state and availability of resources.

17. Explain the use of Labels and Selectors in Kubernetes.
Labels and Selectors are essential sections in Kubernetes configuration files for deployments and services due to how they link Kubernetes services to pods. Labels are key-value pairs that identify pods distinctly; the deployment assigns these labels and uses them as a starting point for the pod prior to its creation, and the Selector matches these labels. Labels and selectors combine to create connections between deployments, pods, and services in Kubernetes.

19. What is a Persistent Volume (PV) in Kubernetes?
A Persistent Volume (PV) in Kubernetes is an object that allows pods to access storage from a defined device. This device is usually described via a Kubernetes StorageClass. When a PVC is created individually, it is generated and designated to the specified storage device. This method wins out over pretreated storage classes because it gives a better understanding of the workflow.


In Kubernetes, the **Master Node** is responsible for managing the cluster and orchestrating the workloads running on **Worker Nodes**. It hosts the control plane components that make cluster-wide decisions, manage the state of the cluster, and handle scheduling and updates. Here’s a detailed explanation of each core component of the Master Node:

### 1. **API Server (kube-apiserver)**

   - **Description**: The API Server is the central management entity of the Kubernetes control plane. It acts as the "front-end" of the Kubernetes control plane, exposing the Kubernetes API, which is the primary entry point for all administrative tasks.
   - **Responsibilities**:
     - Receives API requests (from kubectl, other control plane components, or external systems) and processes them.
     - Validates and configures the data for the API objects (e.g., pods, services, deployments).
     - Acts as a gateway to etcd, the cluster’s database, ensuring only valid data is stored.
     - Serves as the communication hub for all other components within the control plane.
   - **Communication**:
     - Users and administrators interact with the API Server using the `kubectl` command-line tool.
     - Other control plane components (e.g., Scheduler, Controller Manager) communicate with the API Server to get information about the state of the cluster or to make changes.

### 2. **Scheduler (kube-scheduler)**

   - **Description**: The Scheduler is responsible for assigning new pods to nodes in the cluster. It watches for new, unscheduled pods and determines the most suitable node for each pod based on resource availability, constraints, and policies.
   - **Responsibilities**:
     - **Node Selection**: When a pod is created, the scheduler checks which nodes have the required resources (CPU, memory, etc.) and meet the specific requirements and constraints (e.g., affinity/anti-affinity rules, taints/tolerations).
     - **Prioritization**: The Scheduler uses various algorithms to rank nodes based on factors like available resources, workload distribution, and policy compliance.
     - **Pod Placement**: Once the Scheduler finds a suitable node, it assigns the pod to that node, and the information is updated in the etcd database via the API Server.
   - **Communication**: The Scheduler continuously watches the API Server for new pods that need scheduling and then writes back its decisions through the API Server.

### 3. **etcd**

   - **Description**: etcd is a distributed key-value store that serves as the backing store for all Kubernetes cluster data. It is a critical component that stores the cluster’s state and configuration, ensuring high availability and consistency.
   - **Responsibilities**:
     - **Cluster State Storage**: etcd stores all cluster-related data, including configuration, node information, pod states, service discovery information, and more.
     - **Consistency and Availability**: etcd uses the Raft consensus algorithm to provide a consistent view of the data, even in a distributed system where multiple etcd instances are running for redundancy.
     - **Recovery**: In the event of a failure, etcd provides a reliable source of truth that allows Kubernetes to recover and restore cluster state.
   - **Communication**: The API Server interacts directly with etcd to read and write cluster data. All other components indirectly interact with etcd through the API Server, ensuring a consistent and secure communication path.

### 4. **Controller Manager (kube-controller-manager)**

   - **Description**: The Controller Manager is a daemon that runs various controllers, each responsible for regulating and maintaining the desired state of different aspects of the cluster (e.g., nodes, pods, services, endpoints).
   - **Responsibilities**:
     - **Node Controller**: Monitors the health of nodes in the cluster, managing node status updates and removing nodes if they go offline for an extended period.
     - **Replication Controller**: Ensures the desired number of pod replicas are running at all times. If pods crash or are deleted, this controller creates new ones to meet the specified count.
     - **Endpoint Controller**: Manages the mapping between services and pods, ensuring services have the correct endpoints for communication.
     - **Service Account & Token Controller**: Manages service accounts and access tokens for authentication and authorization purposes within the cluster.
   - **Communication**: The Controller Manager constantly watches the cluster state through the API Server and makes adjustments as needed by updating the desired state. It ensures the cluster is operating as defined by user-specified configurations and manifests.

### **Summary of Control Plane Components**

- **API Server**: Central communication hub and front-end for all Kubernetes operations. It validates and configures API requests and communicates with etcd to store cluster data.
- **Scheduler**: Determines where pods should run based on resource availability and policy constraints.
- **etcd**: Distributed key-value store holding the state of the cluster. Acts as the single source of truth for cluster configuration and status.
- **Controller Manager**: Manages various controllers responsible for ensuring the cluster state matches the desired configuration.

These components work together to manage the lifecycle of applications and ensure the cluster remains functional, scalable, and resilient.


WORKER NODE:
  Kubelet: Agent makesure that container is running in pods
  pod:
  kube-proxy: Matains network rules for comm with pods
  container-runtime: A tool responsible for running containerss

The **Worker Node** in Kubernetes is responsible for running the application workloads (pods) and managing the execution of containerized applications. It contains the services and agents necessary to interact with the master node, run pods, and manage network communication. Here’s a breakdown of each component in the worker node:

### 1. **Kubelet**

   - **Description**: The Kubelet is the primary agent running on each worker node. It ensures that the containers described in a PodSpec (pod specification) are running as expected and in the desired state.
   - **Responsibilities**:
     - **Pod Management**: The Kubelet continuously monitors pods scheduled to its node and ensures that the required containers are running. If a container crashes or is deleted, the Kubelet attempts to restart it.
     - **Reporting Node Status**: It gathers information about the state of the node (CPU usage, memory usage, etc.) and sends this data to the API Server, making it available for scheduling and scaling decisions.
     - **Liveness and Readiness Probes**: The Kubelet performs health checks (liveness and readiness probes) on the running containers. If a liveness probe fails, the Kubelet restarts the container; if a readiness probe fails, the container is temporarily removed from service until it is ready again.
   - **Communication**: The Kubelet communicates with the API Server to receive pod specifications and report the node’s status. It also interacts with the container runtime to manage the lifecycle of containers.

### 2. **Pod**

   - **Description**: A pod is the smallest and simplest Kubernetes object. It represents a single instance of a running process in the cluster. A pod can contain one or more containers that share the same network namespace, storage, and configuration.
   - **Characteristics**:
     - **Multi-Container Pods**: Although a pod usually contains a single container, it can host multiple tightly-coupled containers that share resources and need to be co-located (e.g., a web server and a sidecar logging agent).
     - **Networking**: All containers within a pod share the same IP address and network ports, allowing them to communicate via `localhost`.
     - **Storage**: Pods can use persistent storage volumes to store and share data across containers.
   - **Lifecycle**: Pods are ephemeral. If a pod crashes or is deleted, Kubernetes replaces it with a new pod. However, this new pod is not an exact replica; it gets a new IP address and identity, though it remains managed by the same controller (e.g., Deployment, StatefulSet).

### 3. **Kube-Proxy**

   - **Description**: Kube-Proxy is a network proxy that runs on each worker node. It maintains network rules and routes traffic to the correct pods and services.
   - **Responsibilities**:
     - **Service Discovery and Load Balancing**: Kube-Proxy ensures that traffic coming into a node is routed to the appropriate pod based on Kubernetes services. It load-balances network traffic among the pods associated with a service.
     - **IP Tables/IPVS Rules**: Kube-Proxy sets up rules using IP tables or IPVS to manage routing and forwarding network packets to the correct pods.
     - **Managing Network Policies**: It enforces networking policies that define how pods communicate with each other and external services.
   - **Communication**: Kube-Proxy continuously watches the API Server for updates to services and endpoints, updating its rules to match the current state of the cluster.

### 4. **Container Runtime**

   - **Description**: The container runtime is the software responsible for running and managing containers on a node. Kubernetes supports multiple container runtimes, such as Docker, containerd, and CRI-O, through the **Container Runtime Interface (CRI)**.
   - **Responsibilities**:
     - **Starting and Stopping Containers**: The container runtime is responsible for pulling container images, starting containers, and stopping them when no longer needed.
     - **Resource Management**: It ensures that containers run with the required resources (CPU, memory, etc.) as specified in the pod definition.
     - **Interacting with Kubelet**: The container runtime interfaces with the Kubelet, which instructs it to manage container lifecycle operations (start, stop, and report container status).
   - **Popular Container Runtimes**:
     - **Docker**: A well-known container runtime but now deprecated in Kubernetes 1.20+ in favor of containerd or CRI-O.
     - **containerd**: A lightweight and fast runtime derived from Docker’s core components, and now the default runtime for many Kubernetes distributions.
     - **CRI-O**: A runtime built specifically for Kubernetes, designed to provide a minimal, CRI-compliant container runtime.

### **Summary of Worker Node Components**

- **Kubelet**: The primary agent responsible for managing pod lifecycle and ensuring containers are running correctly. It communicates with the API server and interacts with the container runtime.
- **Pod**: The smallest deployable unit in Kubernetes, encapsulating one or more containers that share the same network and storage resources.
- **Kube-Proxy**: Manages networking and routing rules to ensure traffic is directed correctly to the services and pods running on the node.
- **Container Runtime**: Manages the actual containers on the node, pulling images, starting/stopping containers, and interacting with the Kubelet.

Together, these components ensure that applications deployed on Kubernetes run smoothly, efficiently, and securely on the worker nodes.

minikube start/stop
Minikube start
minikube dashboard

kubectl create deployment my-nginx --image=nginx:latest
kubectl get deployments
kubectl get pods
kubectl delete deployement my-app
kubectl expose deployment my-nginx --port=80 --type=LoadBalancer
kubectl get services(list created service)
minikube service my-nginx(provice one url using it we can access application)

kubectl describe pods

kubectl apply -f deployment-node-app.yml
kubectl get deployments
kubectl apply -f service.yml
minikube service my-nginx
kubectl delete -f deployment-node-app.yml