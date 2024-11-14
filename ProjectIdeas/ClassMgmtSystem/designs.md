# Designs

```
class-management-system/
├── public/                     # Public assets, including icons and images
├── src/
│   ├── components/             # Reusable components for UI elements
│   │   ├── Navbar.js           # Navbar for navigation across roles
│   │   ├── Footer.js           # Footer for common information
│   │   ├── Noticeboard.js      # Noticeboard component
│   │   ├── StudentList.js      # Student list display
│   │   ├── MaterialCard.js     # Class material and photos display
│   │   ├── AttendanceTracker.js# Auto Attendance feature
│   │   └── VotingPoll.js       # Poll/Voting UI
│   │
│   ├── pages/                  # Next.js pages
│   │   ├── _app.js             # Custom App component for global styles
│   │   ├── index.js            # Homepage with login options and announcements
│   │   ├── dashboard/          # Role-specific dashboards
│   │   │   ├── admin.js        # Admin dashboard
│   │   │   ├── superAdmin.js   # Super Admin dashboard
│   │   │   ├── student.js      # Student dashboard
│   │   │   ├── cr.js           # Class Representative dashboard
│   │   │   └── ca.js           # Class Administrator dashboard
│   │   ├── auth/               # Authentication pages
│   │   │   ├── login.js        # Login page
│   │   │   └── register.js     # Registration page
│   │   ├── settings/           # User settings pages
│   │   ├── events/             # Events, hackathons, and timeline pages
│   │   └── feedback.js         # Feedback form
│   │
│   ├── services/               # API call wrappers
│   │   ├── authService.js      # Authentication API
│   │   ├── userService.js      # User role management API
│   │   ├── classService.js     # Class data API
│   │   └── fileService.js      # File handling API
│   │
│   ├── store/                  # State management (optional)
│   │   └── store.js            # Redux or Zustand setup for global state
│   │
│   └── styles/                 # CSS/SCSS modules
│       ├── globals.css         # Global styles
│       └── dashboard.module.css# Styles specific to dashboards
│
├── .env.local                  # Environment variables for sensitive data
├── next.config.js              # Next.js configuration for PWA and other settings
└── package.json
```
## High Level App Design 
```plantuml
@startuml
package "Client Layer - Next.js Frontend" {
    [Auth Page]
    [Dashboard]
    [Noticeboard]
    [Student List]
    [Attendance Tracker]
    [Voting Poll]
    [Feedback Page]
}

package "API Layer - Node.js + Express Backend" {
    [Auth API]
    [User Management API]
    [Class/Notice API]
    [File API]
    [Attendance API]
    [Voting/Feedback API]
}

package "Database Layer - MongoDB" {
    [Users Collection]
    [Classes Collection]
    [Notices Collection]
    [Materials Collection]
    [Attendance Collection]
    [Events Collection]
}

package "External Services" {
    [GCS / AWS S3 (File Storage)]
    [Firebase Messaging (Push Notifications)]
    [JWT (Authentication)]
}

[Client Layer - Next.js Frontend] --> [API Layer - Node.js + Express Backend] : HTTP Requests
[API Layer - Node.js + Express Backend] --> [Database Layer - MongoDB]
[API Layer - Node.js + Express Backend] --> [External Services]
@enduml
```
![Img](https://www.plantuml.com/plantuml/png/bP9DZzD038Rl-HNMdefGwO4R1xJTVl0Xkef8OGzL3cvYqi1qPXaxgoB4VyUJ7T910L5o6xz-xSTshbdGItSqsJrMNx0Xk5gObgp0E_n67gPmIoTvzfbXxPqLilKLVCz0lzsyamFaQYaVtqlamzwXh-FxrabRKHeffAlxqYrB3Cqbr4HR4Moz4f2FmaTrsmPoPqoCh8dglQR4dZ-oC_8yVtFcTJK5tgUmEjrxOeORJHk1goNM_S3gsw3LIaUbIvI5GURPunn9UDsQv9cE488f_cnWxfKKUOc2UsGQk3VEDcvvevHdB8Q5pa-LjCwcJ9GAwRh_96nGoBTenbA2FjPM3sGbzVpElpe9UOi62l8FeV40_cfHm0pcTmKKps7IBwiGvzNrP5YWftxs3J5Z4-uyoJi-G9ZXKrjXQCU_ij_URM4IRgOyKLD9MNR_-5DBc4vVmkwYdwE45_1wkytXFNtjY8Mpotonnz-kMVvVcT5Io-nQrUveVW80)

### Mermaid

```mermaid
flowchart TD
    subgraph ClientLayer ["Client Layer - Next.js Frontend"]
        A1["Auth Page"]
        A2["Dashboard"]
        A3["Noticeboard"]
        A4["Student List"]
        A5["Attendance Tracker"]
        A6["Voting Poll"]
        A7["Feedback Page"]
    end

    subgraph APILayer ["API Layer - Node.js + Express Backend"]
        B1["Auth API"]
        B2["User Management API"]
        B3["Class/Notice API"]
        B4["File API"]
        B5["Attendance API"]
        B6["Voting/Feedback API"]
    end

    subgraph DatabaseLayer ["Database Layer - MongoDB"]
        C1["Users Collection"]
        C2["Classes Collection"]
        C3["Notices Collection"]
        C4["Materials Collection"]
        C5["Attendance Collection"]
        C6["Events Collection"]
    end

    subgraph ExternalServices ["External Services"]
        D1["GCS / AWS S3 (File Storage)"]
        D2["Firebase Messaging (Push Notifications)"]
        D3["JWT (Authentication)"]
    end

    ClientLayer -->|HTTP Requests| APILayer
    APILayer --> DatabaseLayer
    APILayer --> ExternalServices

```

```mermaid
flowchart TD
    subgraph ClientLayer ["Next.js App"]
        E1["Auth Page"]
        E2["Dashboard (Role-based)"]
        E3["Noticeboard"]
        E4["Student List"]
        E5["Material Cards"]
        E6["Attendance Tracker"]
        E7["Voting Poll"]
        E8["Feedback Page"]
    end

    subgraph DashboardViews ["Dashboard - Role-based Views"]
        F1["Student View"]
        F2["CR View"]
        F3["Class Admin View"]
        F4["Admin View"]
        F5["Super Admin View"]
    end

    E2 -->|Access based on role| DashboardViews

```

