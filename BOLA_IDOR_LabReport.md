# Lab Report: Broken Object Level Authorization (BOLA / IDOR)

## 1. Executive Summary
* **Lab Module:** API Security Testing — OWASP API Top 10:2023
* **Vulnerability Class:** Broken Object Level Authorization (BOLA / IDOR)
* **Target Application:** OWASP Juice Shop (Dockerized instance on `192.168.56.103:3000`)
* **Status:** Successfully Exploited & Verified

---

## 2. Objective
To test API endpoint access controls by manipulating resource identifiers in HTTP requests. Specifically, the goal was to determine whether an authenticated user (`Account A`) could query and view a distinct user's shopping basket resource (`/rest/basket/{id}`) without authorization checks enforcing ownership.

---

## 3. Lab Environment Setup
* **Attacker Machine:** Kali Linux virtual machine running Burp Suite Community Edition.
* **Target Machine:** Ubuntu Server virtual machine hosting OWASP Juice Shop via Docker (`bkimminich/juice-shop`).
* **Tools Used:** Burp Suite (Proxy, HTTP History, Repeater), Built-in Chromium Browser.

---

## 4. Methodology & Step-by-Step Execution

1. **Account Provisioning:** 
   * Created two independent test accounts (`attacker@test.lab` and `victim@test.lab`) to establish distinct session tokens.
2. **Traffic Capture:** 
   * Intercepted web traffic via Burp Suite Proxy while interacting with the application's shopping cart.
   * Identified the basket retrieval endpoint: `GET /rest/basket/6`.
3. **Repeater Triage:** 
   * Right-clicked the target request in Burp's HTTP History and sent it to **Repeater**.
   * Confirmed the session token in the `Authorization: Bearer <TOKEN>` header mapped to the attacker account.
4. **ID Manipulation:** 
   * Modified the endpoint path from the attacker's assigned resource ID to target a foreign basket identifier (`/rest/basket/6`).
5. **Execution:** 
   * Sent the modified request to observe whether the backend application enforced authorization checks.

---

## 5. Findings & Proof of Concept

* **Request Sent:**
  ```http
  GET /rest/basket/6 HTTP/1.1
  Host: 192.168.56.103:3000
  Authorization: Bearer eyJhbGciOi... [Attacker Token]
