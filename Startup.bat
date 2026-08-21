@echo off
echo ? Starting Avatar Factory Automation Environment...
start /b python TOOLS/auto_backup_daemon.py
python build_factory.py
python factory_simulation.py
echo ?? Workspace status checked and background auto-backup daemon is active.
pause
