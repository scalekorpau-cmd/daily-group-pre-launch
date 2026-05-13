Tracking files
----------------
master-tracker.csv     All tasks (258+). Columns: Owner, Status, Due_Date, Evidence_Link, Notes — fill as you execute.
by-brand\*.csv         Same rows filtered by Brand (plus all.csv for Brand=ALL).

Regenerate from checklist definition (overwrites CSVs):
  py C:\Users\DELL\daily-group-pre-launch\tracking\build_tracker.py

Edit the task list in: build_tracker.py (ROWS / add() calls), then re-run.

Completed rows that must survive regeneration: edit TASK_COMPLETION at the top of
build_tracker.py (Status, Evidence_Link, Notes). All other rows reset to TODO on each run.

If you maintain extra columns only in Excel, export a backup before regenerating.
