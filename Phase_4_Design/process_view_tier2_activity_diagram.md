@startuml
title Tier 2 Task

start
:Log in to System;
  :Check for Assigned Tasks;
  while (Tasks Assigned?) is (true)
    :Retrieve Task;
    :Perform Task;
    :Close Task;
    :Request Manager Records Activity;
    :Wait for Task Assignment;
  endwhile
stop
@enduml
