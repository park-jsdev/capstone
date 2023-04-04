@startuml
actor User

cloud "VPN Server" {
  component Client
  component Intranet {
    component Dashboard
  }
  component "Request Manager" as RM
}

cloud "Database Server" {
  component Database
}

User -> Client
Client --> Intranet
Intranet --> Dashboard
Dashboard --> Database
Dashboard --> Executive
Client --> RM
RM --> Tier1
RM --> Tier2
RM --> Database
@enduml
