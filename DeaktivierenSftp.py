# Stop SFTP Service if not in use

# Set the resource group and storage account name
$resourceGroupName = ""
$storageAccName = ""

# Connect to Azure account
Connect-AzAccount -Identity

# Get the storage account
$storageAccount = Get-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccName

# Check if SFTP is enabled
if ($storageAccount.EnableSftp) {
    # SFTP is currently enabled, so turn it off
    $storageAccount | Set-AzStorageAccount -EnableSftp $false
    Write-Host "SFTP service turned off as it is not in use."
} else {
    Write-Host "SFTP service is already disabled."
}
