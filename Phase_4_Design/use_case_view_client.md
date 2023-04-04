@startuml
left to right direction

actor Client

usecase "Submit a Request" as SR
usecase "Receive Reference Number" as RF1
usecase "Receive Feedback" as RF2

Client --> SR
SR --> RF1
RF1 --> RF2

@enduml