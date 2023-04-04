@startuml
left to right direction

actor Tier1

usecase "Receive Request" as RQ
usecase "Convert Request to Task" as RC
usecase "Assign Task" as AT

Tier1 --> RQ
RQ --> PC
RC --> AT

@enduml