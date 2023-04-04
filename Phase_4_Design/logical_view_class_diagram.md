@startuml
abstract class User {
  -username
  -password
  -email
}

class Executive extends User {
}

abstract class UserType {
  +createRequest()
  +viewRequests()
}

class Tier1 extends UserType {
  +assignTask(task: Task, user: Tier2)
}

class Tier2 extends UserType {
  +performAnalysis(request: Request)
  +performTask(task: Task)
}

class Client extends UserType {
}

class Request {
  -id
  -description
  -status
  -dateLogged
  +updateStatus()
  +addDescription()
}

class RequestManager {
  -requests : List<Request>
  -tasks : List<Task>
  -database : Database
  +updateRequest()
  +assignTask(task: Task, user: Tier2)
  +createTask(task: Task)
  +closeRequest()
}

class AnalysisDashboard {
  -database : Database
  +generateReport()
}

class Database {
  -requests : List<Request>
  -tasks : List<Task>
  +saveRequest(request: Request)
  +saveTask(task: Task)
}

class Task {
  -id
  -description
  -status
  -timestamp
}

class IntranetSite {
  -dashboard : AnalysisDashboard
}

class AnalysisReport {
}


User <|-- UserType
User --> Request : creates >
Request --> RequestManager : submitted to >
Request --> Tier1 : received by >
UserType --> RequestManager : interacts with >
RequestManager --> Database : stores data >
RequestManager --> Tier1 : creates tasks >
Tier1 --> RequestManager : assigns tasks >
RequestManager --> Task : creates tasks >
Task --> Tier2 : completed by >
RequestManager --> Tier2 : assigns tasks >
Tier2 --> RequestManager : closes tasks >
UserType --> AnalysisDashboard : views data >
AnalysisDashboard --> Database : pulls data >
AnalysisDashboard --> AnalysisReport : generates report >
IntranetSite --> AnalysisDashboard : hosts >
Executive --> AnalysisReport : views report >
@enduml