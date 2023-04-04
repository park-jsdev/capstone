@startuml
left to right direction

actor Tier2

usecase "Receive Task" as RT
usecase "Perform Task outside System" as PT
usecase "Close Task" as CT

Tier2 --> RT
RT --> PT
PT --> CT

@enduml