# Research: Native Client (Running X86) code directly from browser

Native client for me traditionally means not interpreted by a virtual execution environment or sandbox but executed by the CPU and bound to the operating system (think Win32). I'd contrast native with HTML, JVM, CLR, etc.

I'm pretty sure that at present, the term Native Client is only used to refer to Google Native Client (NaCl), which is a tool for running native code from within a browser, and yes in this case, Google definitely can explain it to you.


Here’s a bullet-point breakdown to illustrate how the need for **Native Client (NaCl)** arose and how it fulfills those needs:

---

### **The Need for Native Client (NaCl)**

- **Performance Demands:**
  - Native code runs directly on the **CPU** and can fully utilize hardware resources, offering higher performance.
  - **Web applications** (e.g., games, video editing, simulations) require **high-performance computing** that interpreted languages like JavaScript can’t provide efficiently.
  - Executing **compute-intensive tasks** in the browser demands near-native performance, which standard web technologies cannot achieve.

- **Security Concerns:**
  - Running **untrusted native code** directly on a system opens up serious **security vulnerabilities** (e.g., unauthorized access to files or hardware resources).
  - Native code has **direct access to hardware** and can potentially **exploit system weaknesses** if not properly isolated.
  - There is a need for a system to run **untrusted code safely** while protecting the underlying system from malicious attacks.

- **Portability Issues:**
  - Native code is usually **architecture-specific** (e.g., x86, ARM) and tied to an operating system (e.g., Windows, Linux, macOS), making it difficult to run the same code across multiple platforms.
  - Developers need a way to write native code once and have it run on **different hardware architectures** without having to rewrite or recompile it for each platform.

---

### **How Native Client (NaCl) Fulfills the Need**

- **Sandboxing for Security:**
  - NaCl runs native code in a **sandbox**—an isolated environment that restricts the code’s access to system resources.
  - It enforces strict rules through **code validation** to prevent malicious actions, such as unauthorized system calls or memory access.
  - By isolating the native code, NaCl allows **untrusted code** to run **securely** within the browser without risking system integrity.

- **High Performance:**
  - NaCl allows native code to run at **near-native speeds** directly within a web browser, combining the speed of native execution with the convenience of web applications.
  - It leverages native CPU instruction sets (e.g., x86) for **optimal performance**, making it ideal for **high-performance web apps** like 3D games, simulations, and data processing.

- **Cross-Platform Portability:**
  - NaCl ensures **portability** by enabling the same native code to run on **multiple operating systems** (Windows, Linux, macOS) with minimal modification.
  - It supports various **instruction sets** (x86, ARM, MIPS) and uses architecture-neutral APIs to make native code run smoothly across different platforms.
  - Developers can write code once and run it anywhere NaCl is supported, reducing the effort of maintaining multiple versions of the same application.

- **Controlled Access to Resources:**
  - NaCl limits access to **system resources** through controlled APIs, allowing only secure and approved interactions with hardware and system files.
  - Only **whitelisted system calls** are allowed, ensuring the code cannot perform unsafe operations or access sensitive system information.

---

This outline shows how **Native Client (NaCl)** addresses the critical issues of **performance, security**, and **portability** when running native code in web environments.

# Presentation

# Slide: 

