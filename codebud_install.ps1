# Define the URL and destination path
$Url = "https://github.com/mitchtasso/CodeBud/raw/refs/heads/main/codebud.exe"
$Destination = "$env:USERPROFILE\Codebud\codebud.exe"

New-Item -Path "$env:USERPROFILE\Codebud\" -ItemType Directory -Force

# Download the file
Invoke-WebRequest -Uri $Url -OutFile $Destination

# Get the directory of the downloaded file
$Dir = Split-Path $Destination

# Add the directory to the PATH (User-level)
$CurrentPath = [Environment]::GetEnvironmentVariable("Path", "User")

if ($CurrentPath -notlike "*$Dir*") {
    $NewPath = "$CurrentPath;$Dir"
    [Environment]::SetEnvironmentVariable("Path", $NewPath, "User")
    Write-Output "Added $Dir to PATH."
} else {
    Write-Output "$Dir is already in PATH."
}

# Optional: Refresh PATH in current session
$env:Path = [Environment]::GetEnvironmentVariable("Path", "User")
