$process1Name = "process1"
$process1Path = "path1"
$process2Name = "process2"
$process2Path = "path2"
$extension = ".exe"

while ($true) {
    $process1 = Get-Process -Name $process1Name -ErrorAction SilentlyContinue
    $process2 = Get-Process -Name $process2Name -ErrorAction SilentlyContinue
    $currentTime = Get-Date -Format "[yyyy-MM-dd HH:mm:ss]"
    if ($process1 -and $process2) {
        Write-Host "$currentTime $process1Name and $process2Name are already running."
    } else {
        if (!$process1) {
            Write-Host "$currentTime $process1Name is not running. Starting $process1Name..."
            Start-Process -FilePath $process1Name$extension -WorkingDirectory $process1Path
        }
        if (!$process2) {
            Write-Host "$currentTime $process2Name is not running. Starting $process2Name..."
            Start-Process -FilePath $process2Name$extension -WorkingDirectory $process2Path
        }
    }
    Start-Sleep -Seconds 60
}
