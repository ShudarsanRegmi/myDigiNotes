# Why so weird directory structure in linux
The directory structure in Linux, while it may seem complex at first, has historical and practical reasons behind it. Here's a breakdown of the directories you've mentioned and their purposes:

### `/usr/lib`
- **Purpose**: Contains shared libraries and binaries for programs that are installed from the system's package manager.
- **Usage**: This is the standard directory where shared libraries (files needed by multiple programs) are placed. It includes files that are required for the operation of software installed via the package management system of the distribution (e.g., `apt`, `yum`).

### `/usr/local/lib`
- **Purpose**: Contains shared libraries for software that is manually installed by the system administrator (not from the package manager).
- **Usage**: This directory is used for libraries that are locally compiled or installed by the user/administrator. It's meant to keep manually installed software separate from the distribution-provided software.

### `/usr/lib64`
- **Purpose**: Contains 64-bit shared libraries.
- **Usage**: On 64-bit systems, this directory is used to store 64-bit libraries. This distinction is important in systems that support multi-architecture binaries (both 32-bit and 64-bit).

### `/usr/local/lib64`
- **Purpose**: Would contain 64-bit shared libraries for manually installed software.
- **Usage**: This directory is not present on all systems. Its presence depends on the conventions of the specific distribution and the need to segregate 64-bit libraries of locally installed software.

### Why These Directories Exist

1. **Separation of Concerns**: 
   - **`/usr/lib` vs. `/usr/local/lib`**: The separation allows the system to distinguish between software installed by the package manager (`/usr/lib`) and software installed manually by the user (`/usr/local/lib`). This helps in managing and upgrading software without conflicts.
   
2. **Architecture Differentiation**: 
   - **`/usr/lib` vs. `/usr/lib64`**: On systems that support multiple architectures (e.g., 32-bit and 64-bit), it's essential to have separate directories to avoid conflicts and ensure that the correct version of a library is used by applications. This is why `lib` and `lib64` directories exist.

3. **Local Software Management**:
   - **`/usr/local/lib64`**: Although not always present, this directory can be used to follow the same separation logic for 64-bit libraries of locally installed software, just as `/usr/local/lib` is used for 32-bit libraries or architecture-agnostic libraries.

### Why `/usr/local/lib64` Might Be Missing

- **System Configuration**: Not all distributions create a `/usr/local/lib64` directory by default. It depends on the distribution's policies and whether the user or administrator has installed 64-bit libraries manually.
- **Need-Based Creation**: The directory may only be created if there's a specific need to separate 64-bit local libraries. If no such libraries are installed, the directory might not exist.

### Summary

The Linux directory structure may seem complex, but it's designed for flexibility and organization. It allows for clear distinctions between system-installed and user-installed software, as well as between different architectures. This organization helps in maintaining the system and ensuring compatibility across different types of software installations.
