	# Set the resource group and storage account name
	$resourceGroupName = ""
	$storageAccName = ""
	
	# Connect to Azure account
	Connect-AzAccount -Identity

	# Get the storage account
	$storageAccount = Get-AzStorageAccount -ResourceGroupName $resourceGroupName -Name $storageAccName
	
	# Check if SFTP is disabled
	if (-not $storageAccount.EnableSftp) {
	    # SFTP is currently disabled, so turn it on
	    $storageAccount | Set-AzStorageAccount -EnableSftp $true
	    Write-Host "SFTP service activated for use."
	} else {
	    Write-Host "SFTP service is already enabled."
	}
