@startuml
title Client Activity

start
:Log in to System;
:Create Request;
:Submit Request;
if (Request is approved by Tier1) then (yes)
  :Request Assigned;
else (no)
  :Request Rejected;
endif
stop
@enduml