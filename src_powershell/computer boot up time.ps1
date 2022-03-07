
write-host "Введите имя ПК (пр. R54-630300IT04):"
$pc_name = read-host

Get-CimInstance -ClassName win32_operatingsystem -ComputerName $pc_name | select csname, lastbootuptime

Pause
