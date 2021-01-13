#define MyAppName "Háromtér"
#define MyAppExeName "haromter.exe"

[Setup]
AppName=Haromter
AppVersion=0.9
DefaultDirName={autopf}\Haromter
OutputBaseFilename=HaromterSetup
LicenseFile=license.txt
DefaultGroupName={#MyAppName}

[Files]
Source: dist\haromter.exe; DestDir: "{app}"


[Tasks]
; Asztali ikon
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
 
[Run]
; Telepítés után futtatás
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
 
[Icons]
; Startmenü 
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon


