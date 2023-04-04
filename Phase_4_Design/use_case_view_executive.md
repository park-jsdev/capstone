@startuml
left to right direction

actor Executive

usecase "Generate Report" as GR
usecase "View Report" as VR2
usecase "View Dashboard" as PBI

Executive --> PBI
PBI --> GR
GR --> VR2

@enduml