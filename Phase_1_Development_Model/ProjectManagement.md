---
title: HR Data Requests
---
graph LR
A -->|T| T{Halfway}
A[HR Data Requests] -->|HRBT| B(PDF Report)
A -->|Agile| C(Capstone Project)
B -->|Complete| D2{HRBT}
C -->|Progress| D((Milestone 1 <br> EOY Fiscal))

T --> T2{EOY Fiscal}
D -->|Progress| E(Power BI Dashboard)

T2 --> T3{Halfway}
E -->|Deploy| F{HRBT}
E -->|Complete| G{School Diploma}

T3 --> T4{Graduation/Contract}
F -->|Develop| H[Full-Scale Application]

T4 --> T5{EOQ1}
H -->|Deploy| I[Project End]

Z[Discoverer Decommissioning]--> Z1[Halfway] -->Z2[Done]