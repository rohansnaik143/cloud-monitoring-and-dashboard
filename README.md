# cloud-monitoring-and-dashboard
Companies need to know when servers are down, overloaded, or costing too much.   This project sets up an AWS CloudWatch monitoring &amp; alerting system for EC2 instances — using only Free Tier resources.



---

## ⚙️ Implementation
1. **EC2 Instance**  
   - Amazon Linux 2 t2.micro  
   - Deployed sample app / SSH access  

2. **CloudWatch Metrics & Agent**  
   - CPU utilization (default)  
   - Memory & disk usage (via CloudWatch Agent)  

3. **CloudWatch Dashboard**  
   - Centralized view of EC2 metrics  

4. **CloudWatch Alarms**  
   - CPU > 70%  
   - Memory > 80%  

5. **SNS Notifications**  
   - Sends Email/SMS when alarm triggers  

---

## 🧪 Testing the Setup
- **CPU Stress Test**
  ```bash
  sudo yum install -y stress
  stress --cpu 1 --timeout 300
