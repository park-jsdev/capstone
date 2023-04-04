@startuml
left to right direction

actor User

node "Intranet Site" {
  component AnalysisDashboard
}

node "Application Server" {
  component RequestManager
}

database "Database" {
  component TaskData
  component RequestData
}

User -> AnalysisDashboard: View Analysis
User -> RequestManager: Submit Request
RequestManager -> TaskData: Store Task Data
RequestManager -> RequestData: Store Request Data
AnalysisDashboard -> RequestData: View Request Data
@enduml