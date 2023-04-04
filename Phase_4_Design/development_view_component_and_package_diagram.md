@startuml
package "Client Interface" {
  [Client]
}

package "Request Management" {
  [RequestManager]
  [Request]
  [Task]
}

package "Analysis" {
  [AnalysisDashboard]
  [AnalysisReport]
}

Database <--> RequestManager
Request -down-> Task
RequestManager -down-> AnalysisDashboard
AnalysisDashboard -down-> AnalysisReport
@enduml