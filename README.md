# blackjackServer
set up SSH server with the given sshd_config
this runs the program as soon as user connects and disconnects them immediately
when it ends (should not let them sus about).

Relevant commands:

Run PowerShell as admin then to edit config do C:\ProgramData\ssh\sshd_config

Get-Service sshd

Start-Service sshd

Stop-Service sshd

Restart-Service sshd


Todo:

Get URL instead of IP

Do not require passwords

Run on server somehow idk you can't do Linux so figure it out
