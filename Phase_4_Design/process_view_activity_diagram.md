@startuml
start
:Create Request;
if (User is Tier1) then (yes)
  :Assign Task;
  if (Task is complete) then (yes)
    :Close Request;
  else (no)

    :Assign Task;
  endif
else (no)
  :Submit Request;
  if (Request is approved) then (yes)
    :Assign Task;
    if (Task is complete) then (yes)
      :Close Request;
    else (no)
      :Assign Task;
    endif
  else (no)
  endif
endif
stop
@enduml
