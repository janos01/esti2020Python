#define MyAppName "H�romt�r"
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
; Telep�t�s ut�n futtat�s
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
 
[Icons]
; Startmen� 
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon


