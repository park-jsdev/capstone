@startuml
title Tier1 Process

start
:Retrieve Request from RequestManager;
while (Requests to Process?) is (true)
  :Convert Request to Task;
  :Assign Task to Tier2 User;
  if (Task Complete?) then (yes)
    :Close Request;
    :Record Request in RequestManager;
  else (no)
  endif
endwhile
stop
@enduml
