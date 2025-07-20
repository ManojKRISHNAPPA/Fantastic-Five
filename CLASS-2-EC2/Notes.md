# Amazon EC2 (Elastic Compute Cloud) — Complete Theory Guide

---

## 1. What is Amazon EC2?
Amazon Elastic Compute Cloud (EC2) is a web service that provides resizable compute capacity in the cloud. It allows users to rent virtual servers (**instances**) to run applications. EC2 offers complete control over the underlying OS and software and supports scaling and flexible configurations.

---

## 2. Key Features of EC2
- Elasticity & Scalability: Scale capacity up/down based on demand.
- Variety of Instance Types: Compute, memory, storage, GPU optimized.
- Custom AMIs: Use or create Amazon Machine Images.
- Security: Integration with IAM, security groups, key pairs.
- Persistent Storage: Elastic Block Store (EBS) volumes.
- Networking: VPC, Elastic IPs, load balancers.
- Flexible Pricing: On-demand, reserved, spot instances.

---

## 3. What is an EC2 Instance?
A virtual server in AWS cloud that can run Linux, Windows, etc. Instance types differ in CPU, memory, storage, and networking.

---

## 4. Types of EC2 Instances
- General Purpose (t3, m5): Balanced.
- Compute Optimized (c5): High CPU.
- Memory Optimized (r5): Large memory.
- Storage Optimized (i3): High IOPS.
- GPU Instances (p3): ML, graphics.
- Burstable (t3): Low baseline with burst capability.

---

## 5. What is an AMI (Amazon Machine Image)?
A template containing OS, apps, and configuration for launching an instance. AMIs can be public, private, or shared.

---

## 6. What is Elastic Block Store (EBS)?
Persistent block storage volumes attached to EC2. Data persists independently of the instance lifecycle. Supports snapshots.

Types:
- General Purpose SSD (gp2/gp3)
- Provisioned IOPS SSD (io1/io2)
- Throughput Optimized HDD (st1)
- Cold HDD (sc1)

---

## 7. Explain Security in EC2
- Security Groups: Virtual firewalls controlling traffic.
- Key Pairs: SSH/RDP authentication.
- IAM Roles: Permissions to access AWS services.
- VPC: Network isolation.

---

## 8. What are EC2 Pricing Models?
- On-Demand: Pay per use, no upfront.
- Reserved: 1 or 3-year commitment, discounted.
- Spot: Bid for unused capacity, interruptible.
- Dedicated Hosts: Physical server reserved.
- Savings Plans: Flexible discount plans.

---

## 9. What is Auto Scaling?
Automatically adjusts the number of instances based on demand using CloudWatch alarms for scaling events.

---

## 10. How does EC2 Networking work?
- Instances launched in VPC.
- Private IPs by default; optional public IPs.
- Elastic IPs: Static public IPs.
- ENI: Virtual network interfaces.
- Load Balancers distribute traffic.

---

## 11. Instance Store vs EBS
- Instance Store: Temporary, physically attached storage; data lost on stop/terminate.
- EBS: Persistent, network-attached storage; data persists beyond instance lifecycle.

---

## 12. What is a Placement Group?
Logical grouping of instances in an AZ to achieve low latency or fault tolerance.

Types:
- Cluster: Low latency, high throughput.
- Spread: Spread across hardware to reduce correlated failures.
- Partition: Divides instances into logical partitions.

---

## 13. How to Connect to EC2?
- Linux: SSH with private key.
- Windows: RDP using decrypted password.

---

## 14. What is Elastic Load Balancing (ELB)?
Distributes incoming traffic across multiple instances.

Types:
- Classic Load Balancer
- Application Load Balancer (Layer 7)
- Network Load Balancer (Layer 4)

---

## 15. Stop vs Terminate Instance
- Stop: Instance shut down, data preserved, restartable.
- Terminate: Instance and root volume deleted permanently.

---

## 16. How does EC2 ensure high availability?
- Use multiple Availability Zones (AZs).
- Auto Scaling with Load Balancers.
- Backups via snapshots/AMIs.
- Multi-AZ architectures.

---

## 17. Can you resize an EC2 instance?
Yes. Stop the instance, change the instance type, then restart.

---

## 18. What is User Data?
Scripts or commands run on instance launch for automation/configuration.

---

## 19. What are Spot Instances?
Instances using spare AWS capacity at a discount, interruptible with 2 minutes notice. Ideal for fault-tolerant and flexible workloads.

---

## 20. Common Use Cases of EC2
- Hosting websites/apps.
- Big data processing.
- HPC (High Performance Computing).
- ML model training.
- Backend servers.
- Disaster recovery.

---

# Summary Table

| Concept               | Description                                 |
|-----------------------|---------------------------------------------|
| EC2 Instance          | Virtual server in AWS cloud                  |
| AMI                   | Template for instance launch                 |
| EBS                   | Persistent block storage                      |
| Security Groups       | Firewall rules for instance traffic          |
| Key Pair              | SSH/RDP authentication                        |
| Pricing Models        | On-demand, Reserved, Spot, Dedicated         |
| Placement Groups      | Low latency or fault tolerant grouping       |
| Auto Scaling          | Automatic instance scaling                     |
| Elastic Load Balancer | Distributes traffic among instances           |
| User Data             | Initialization scripts on boot                 |
| Instance Store        | Temporary local storage                         |
| VPC                   | Virtual private cloud network                  |

---

